from typing import List, Dict
import random

# Initial prompt to start extracting user preferences
INITIAL_PROMPT = """You are a career guidance assistant. Please help me understand your interests and preferences.
Let's start with some basic questions:

1. What subjects or topics do you enjoy learning about?
2. What activities do you find most engaging in your free time?
3. What kind of work environment do you prefer (e.g., office, outdoors, remote)?
4. Do you prefer working independently or in teams?
5. What are your strengths and skills?

Please share your thoughts on these questions."""

# Follow-up prompts to dig deeper into specific categories
FOLLOW_UP_PROMPTS = {
    "interests": "Could you tell me more about your interest in {context}? What specifically draws you to it?",
    "skills": "You mentioned {context} as a strength (or it's implied). How have you developed this skill, and how do you enjoy using it?",
    "environment": "Considering {context}, what specific aspects of your ideal work environment are most important to you?",
    "values": "Beyond {context}, what values are most important to you in a career? (e.g., creativity, stability, helping others)",
    "lifestyle": "Thinking about a career in {context}, how do you envision your work-life balance? What kind of schedule or demands would you prefer?"
}

# Clarifying questions as fallback prompts
CLARIFYING_QUESTIONS = [
    "Could you elaborate on that?",
    "What do you mean by that?",
    "Could you give me an example?",
    "How does that make you feel?",
    "What aspects of that interest you the most?"
]

# Prompt template for extracting interests from conversation using Mistral
EXTRACT_INTERESTS_PROMPT = """You are an expert career guidance assistant. Your primary goal is to extract concise, actionable keywords and preferences from the entire conversation history that can directly map to career categories. Focus on terms related to fields (e.g., science, technology, business, arts, health, education), skills (e.g., programming, analysis, design, writing, teaching), and work activities (e.g., research, management, care, performance). Combine and refine all relevant terms across turns. Return them as a comma-separated list of single or short phrases (e.g., 'data analysis', 'creative writing', 'patient care')."""

# Template for generating short explanations for recommended career paths
CAREER_PATH_EXPLANATION_TEMPLATE = """Provide a concise and clear explanation for the career path: {career_path}. Highlight the key aspects, typical roles, and what makes this path unique and rewarding."""

def get_initial_prompt() -> str:
    return INITIAL_PROMPT

def get_follow_up_prompt(category: str, context: str) -> str:
    return FOLLOW_UP_PROMPTS.get(category, "").format(context=context)

def get_clarifying_question() -> str:
    return random.choice(CLARIFYING_QUESTIONS)

def get_extract_interests_prompt() -> str:
    return EXTRACT_INTERESTS_PROMPT

def get_career_path_explanation_prompt(career_path: str) -> str:
    return CAREER_PATH_EXPLANATION_TEMPLATE.format(career_path=career_path)
