import os
from typing import List, Dict, Tuple
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai import Mistral

from prompt_templates import (
    get_initial_prompt,
    get_follow_up_prompt,
    get_clarifying_question,
    get_extract_interests_prompt,
    get_career_path_explanation_prompt
)
from career_paths import (
    map_interests_to_careers,
    get_career_description,
    get_career_options,
    get_career_roadmap
)

load_dotenv()

class CareerRecommender:
    def __init__(self):
        self.client = MistralClient(
            api_key=os.getenv("MISTRAL_API_KEY")
        )
        self.conversation_history = []
        self.last_ai_prompt_content = None # To detect repetitive prompts
        self.last_topic_queried = None # To track the last topic asked about
        self.consecutive_same_topic_count = 0 # To count consecutive questions on the same topic
        self.follow_up_categories = ["interests", "skills", "environment", "values", "lifestyle"] # Categories for cycling prompts
        self.follow_up_category_index = 0 # Index to cycle through categories
        
    def start_conversation(self) -> str:
        """Starts the career guidance conversation."""
        initial_prompt = get_initial_prompt()
        self.last_ai_prompt_content = initial_prompt # Store initial prompt
        self.last_topic_queried = None # Reset on new conversation
        self.consecutive_same_topic_count = 0 # Reset on new conversation
        self.follow_up_category_index = 0 # Reset for a new conversation
        return initial_prompt
    
    def process_response(self, user_response: str) -> Tuple[str, List[Dict]]:
        """
        Processes user response and returns next prompt and career recommendations.
        Returns a tuple of (next_prompt, career_recommendations)
        """
        self.conversation_history.append({"role": "user", "content": user_response})
        
        # Extract interests from the conversation
        interests = self._extract_interests()
        
        # Map interests to career paths
        career_matches = map_interests_to_careers(interests)
        
        # Generate recommendations
        recommendations = []
        for path, confidence in career_matches[:3]:  # Top 3 matches
            if confidence > 0.01:  # Lowered threshold to 1% to get more matches
                recommendations.append({
                    "path": path,
                    "confidence": confidence,
                    "description": get_career_description(path),
                    "careers": get_career_options(path),
                    "roadmap": get_career_roadmap(path)
                })
        
        # Determine the next prompt based on recommendations
        next_prompt = ""
        if not recommendations:
            next_prompt = "I need more information to provide better career recommendations. Could you elaborate on your **favorite subjects/topics, hobbies/activities, or specific skills**?"
            self.last_topic_queried = None # Reset topic tracking
            self.consecutive_same_topic_count = 0 # Reset consecutive topic count
            self.follow_up_category_index = 0 # Reset index if no recommendations are found
        else:
            # Use the highest confidence match for follow-up
            top_match = recommendations[0]
            
            # --- Logic to prevent getting stuck on the same topic ---
            if self.last_topic_queried == top_match["path"]:
                self.consecutive_same_topic_count += 1
            else:
                self.consecutive_same_topic_count = 0 # Reset if topic changes
                self.last_topic_queried = top_match["path"] # Update last queried topic
            
            if self.consecutive_same_topic_count >= 2: # If the same topic is asked about 2 or more times consecutively
                next_prompt = "It seems we're focused on \"" + top_match["path"] + "\". To help me understand your broader interests, could you share completely new subjects, activities, or skills you haven't mentioned yet?"
                self.consecutive_same_topic_count = 0 # Reset counter after forcing broader question
                self.last_topic_queried = None # Reset topic tracking to allow new focus
                self.follow_up_category_index = 0 # Reset index to start cycling from beginning after a hard break
            else:
                # Cycle through follow-up categories
                current_category = self.follow_up_categories[self.follow_up_category_index]
                next_prompt = get_follow_up_prompt(current_category, top_match["path"])
                self.follow_up_category_index = (self.follow_up_category_index + 1) % len(self.follow_up_categories)
            # --- END Logic ---

            # Failsafe: Force broad question after N turns if still stuck on topic-specific 
            # Each turn adds 2 messages (user + assistant). So 6 messages = 3 turns.
            if len(self.conversation_history) >= 6 and "Could you tell me more about your interest in" in next_prompt and "It seems we're focused on" not in next_prompt:
                next_prompt = "We've explored this topic quite a bit. To help me find more diverse recommendations, could you tell me about entirely new interests, skills, or preferences you haven't mentioned yet, or what you'd like to do next?"
                self.consecutive_same_topic_count = 0 # Reset topic counter too for this hard reset
                self.last_topic_queried = None
                self.follow_up_category_index = 0 # Reset index after a hard break
        
        self.last_ai_prompt_content = next_prompt # Store this prompt for the next turn
        self.conversation_history.append({"role": "assistant", "content": next_prompt})
        return next_prompt, recommendations
    
    def _extract_interests(self) -> List[str]:
        """Extracts interests from the entire conversation history using Mistral AI."""
        messages = []
        # Add system message first
        messages.append(ChatMessage(role="system", content=get_extract_interests_prompt()))
        
        # Add entire conversation history
        for msg in self.conversation_history:
            messages.append(ChatMessage(role=msg["role"], content=msg["content"])) # Re-add all messages
        
        response = self.client.chat(
            model="mistral-medium",
            messages=messages,
            temperature=0.3 # Lower temperature for more deterministic extraction
        )
        
        # Clean and split the response
        interests = [interest.strip() for interest in response.choices[0].message.content.split(",")]
        print(f"Extracted interests from Mistral: {interests}") # Debugging line
        return interests

def format_recommendations(recommendations: List[Dict]) -> str:
    """Formats career recommendations into a professional, structured format."""
    if not recommendations:
        return "I need more information to provide career recommendations. Could you tell me more about your interests?"
    
    output = "Career Path Recommendations\n"
    output += "=" * 30 + "\n\n"
    
    for rec in recommendations:
        # Career Path Header
        output += f"Career Path: {rec['path']}\n"
        output += f"Match Confidence: {rec['confidence']:.0%}\n"
        output += "-" * 30 + "\n"
        
        # Description
        output += "Overview:\n"
        output += f"{rec['description']}\n\n"
        
        # Career Options
        output += "Recommended Career Options:\n"
        for i, career in enumerate(rec['careers'][:3], 1):
            output += f"{i}. {career}\n"
        output += "\n" + "=" * 30 + "\n\n"
    
    return output 
