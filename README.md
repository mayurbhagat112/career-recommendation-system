# Career Recommendation System

An intelligent career guidance system that leverages natural language processing and AI to understand user interests and provide personalized career recommendations across diverse fields including STEM, Arts, Business, Healthcare, Education, and Sports.

## Features

- Interactive conversation-based interface powered by Streamlit
- AI-driven extraction of user interests and preferences using Mistral AI
- Mapping of interests to predefined career paths with confidence scoring
- Detailed career path descriptions, recommended careers, and roadmaps
- Support for a wide range of career paths including STEM, Arts, Business, Healthcare, Education, and Sports
- Follow-up prompts to refine recommendations and gather more user input
- Professional and user-friendly UI with session state management

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd career-recommendation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Mistral API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app to start an interactive career guidance session:

```bash
streamlit run app.py
```

The system will:

1. Ask initial questions about your interests and preferences
2. Process your responses to extract key interests using AI
3. Map your interests to potential career paths with confidence scores
4. Provide detailed recommendations including career options and roadmaps
5. Ask follow-up questions to refine and improve recommendations

## Project Structure

- `app.py`: Streamlit web application providing the user interface
- `career_recommender.py`: Core recommendation system implementation using Mistral AI
- `career_paths.py`: Defines predefined career paths, keywords, career options, descriptions, and roadmaps
- `prompt_templates.py`: Contains AI prompt templates for conversation and interest extraction
- `requirements.txt`: Python dependencies
- `.env`: Environment variables including API keys (not included in repo)

## Career Paths Included

- **STEM**: Science, Technology, Engineering, Mathematics, AI, Robotics, Cybersecurity
- **Arts**: Design, Music, Writing, Photography, Film, Theater
- **Business**: Management, Finance, Marketing, Consulting, Real Estate, Logistics
- **Healthcare**: Medical, Nursing, Therapy, Dentistry, Veterinary, Nutrition
- **Education**: Teaching, Training, E-learning, Instructional Design
- **Sports**: Athletics, Coaching, Sports Medicine, Refereeing, Sports Analytics

## Customization

You can customize the system by:

- Adding new career paths or expanding keywords in `career_paths.py`
- Modifying AI prompt templates in `prompt_templates.py`
- Adjusting confidence thresholds or recommendation logic in `career_recommender.py`
- Enhancing the UI in `app.py`

## Requirements

- Python 3.8+
- Mistral API key
- Required Python packages listed in `requirements.txt`

## License

This project is licensed under the MIT License.

---

Created by Mayur Bhagat
