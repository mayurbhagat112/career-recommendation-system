import streamlit as st
from career_recommender import CareerRecommender, format_recommendations

# Page configuration
st.set_page_config(
    page_title="Career Path Recommender",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling and layout improvements
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Theme variables */
    :root {
        /* Dark theme (default) */
        --primary-color: #4a5568;
        --secondary-color: #718096;
        --background-color: #1a202c;
        --card-background: #2d3748;
        --text-primary: #f7fafc;
        --text-secondary: #a0aec0;
        --success-color: #48bb78;
        --warning-color: #ecc94b;
        --danger-color: #f56565;
        --button-hover: #2d3748;
        --border-color: #4a5568;
        --input-background: #2d3748;
        --shadow-color: rgba(0, 0, 0, 0.1);
        --button-primary: #4299e1;
        --button-primary-hover: #3182ce;
        --button-secondary: #4a5568;
        --button-secondary-hover: #2d3748;
        --button-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --button-hover-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    /* Light theme */
    @media (prefers-color-scheme: light) {
        :root {
            --primary-color: #2563eb;
            --secondary-color: #3b82f6;
            --background-color: #f8fafc;
            --card-background: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --success-color: #059669;
            --warning-color: #d97706;
            --danger-color: #dc2626;
            --button-hover: #1d4ed8;
            --border-color: #e2e8f0;
            --input-background: #ffffff;
            --shadow-color: rgba(0, 0, 0, 0.05);
            --card-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
            --hover-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --button-primary: #3b82f6;
            --button-primary-hover: #2563eb;
            --button-secondary: #94a3b8;
            --button-secondary-hover: #64748b;
            --button-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --button-hover-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
    }

    /* Global styles */
    body {
        color: var(--text-primary);
        background-color: var(--background-color);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.6;
    }

    [data-testid="stAppViewContainer"] {
        background-color: var(--background-color);
        padding: 2rem 3rem;
    }

    .main {
        padding: 3rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Typography improvements */
    h1 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 1.5rem !important;
        letter-spacing: -0.025em !important;
        line-height: 1.2 !important;
    }

    h2 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        font-size: 2rem !important;
        margin: 2rem 0 1rem !important;
        letter-spacing: -0.025em !important;
    }

    h3 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        margin: 1.5rem 0 1rem !important;
        letter-spacing: -0.025em !important;
    }

    h4 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        font-size: 1.25rem !important;
        margin: 1.25rem 0 0.75rem !important;
    }

    p {
        color: var(--text-secondary) !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        margin-bottom: 1rem !important;
    }

    strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }

    /* Input field styling */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: var(--input-background) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 1.1rem !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--card-shadow) !important;
    }

    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.1) !important;
        outline: none !important;
    }

    /* Recommendation box styling */
    .recommendation-box {
        background-color: var(--card-background);
        padding: 1.75rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border: 1px solid var(--border-color);
        box-shadow: var(--card-shadow);
        transition: all 0.2s ease;
    }

    .recommendation-box:hover {
        transform: translateY(-2px);
        border-color: var(--primary-color);
        box-shadow: var(--hover-shadow);
    }

    .recommendation-box h3 {
        color: var(--text-primary) !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-bottom: 1.25rem !important;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        letter-spacing: -0.025em !important;
    }

    .recommendation-box p {
        color: var(--text-secondary) !important;
        line-height: 1.7 !important;
        margin: 1rem 0 !important;
        font-size: 1.1rem !important;
    }

    .recommendation-box ol,
    .recommendation-box ul {
        margin: 1rem 0 !important;
        padding-left: 1.5rem !important;
    }

    .recommendation-box li {
        color: var(--text-secondary) !important;
        margin: 0.5rem 0 !important;
        line-height: 1.6 !important;
        font-size: 1.1rem !important;
    }

    /* Confidence badge styling */
    .confidence-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.35em 0.75em;
        font-size: 0.875rem;
        font-weight: 600;
        border-radius: 9999px;
        color: white !important;
        letter-spacing: 0.025em;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }

    .confidence-high {
        background-color: var(--success-color) !important;
    }

    .confidence-medium {
        background-color: var(--warning-color) !important;
        color: white !important;
    }

    .confidence-low {
        background-color: var(--danger-color) !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: var(--button-primary);
        color: white !important;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
        font-size: 1.1rem;
        font-family: 'Inter', sans-serif;
        transition: all 0.2s ease;
        letter-spacing: 0.025em;
        box-shadow: var(--button-shadow);
        position: relative;
        overflow: hidden;
    }

    .stButton>button:hover {
        background-color: var(--button-primary-hover);
        transform: translateY(-1px);
        box-shadow: var(--button-hover-shadow);
    }

    .stButton>button:active {
        transform: translateY(0);
        box-shadow: var(--button-shadow);
    }

    /* Secondary button styling */
    .stButton>button[data-baseweb="button"][kind="secondary"] {
        background-color: var(--button-secondary);
        color: white !important;
        border: 1px solid var(--border-color);
    }

    .stButton>button[data-baseweb="button"][kind="secondary"]:hover {
        background-color: var(--button-secondary-hover);
        border-color: var(--button-secondary-hover);
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--card-background);
        border-right: 1px solid var(--border-color);
    }

    .sidebar .sidebar-content {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }

    /* Footer styling */
    footer {
        text-align: center;
        padding: 1.5rem 0;
        color: var(--text-secondary);
        font-size: 0.95rem;
        background-color: var(--card-background);
        border-top: 1px solid var(--border-color);
        font-family: 'Inter', sans-serif;
    }

    footer a {
        color: var(--primary-color) !important;
        text-decoration: none;
        transition: color 0.2s ease;
        font-weight: 500;
    }

    footer a:hover {
        color: var(--secondary-color) !important;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2rem !important;
        }
        
        h2 {
            font-size: 1.75rem !important;
        }
        
        h3 {
            font-size: 1.35rem !important;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            font-size: 1rem;
        }
        
        .recommendation-box {
            padding: 1.25rem;
        }
        
        p, .recommendation-box p, .recommendation-box li {
            font-size: 1rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with app description and instructions
with st.sidebar:
    st.title("About")
    st.markdown("""
    ### 🎯 Career Path Recommender
    
    An AI-powered platform that helps you discover your ideal career path based on your unique interests, skills, and preferences.

    #### How to Use:
    1. Share your interests and skills
    2. Answer follow-up questions
    3. Get personalized career recommendations
    4. Explore detailed career roadmaps

    Built with Streamlit and Mistral AI
    """)
    
    st.markdown("---")
    st.markdown("Created by Mayur Bhagat")

# Initialize session state for conversation management
if 'recommender' not in st.session_state:
    st.session_state.recommender = CareerRecommender()
    st.session_state.display_history = []
    st.session_state.current_prompt = st.session_state.recommender.start_conversation()
    st.session_state.current_input_value = ""
    st.session_state.conversation_started = False

# Function to handle submission and process input
def handle_submit():
    user_input = st.session_state.user_input_form_key
    if user_input:
        with st.spinner("Analyzing your interests..."):
            next_prompt, recommendations = st.session_state.recommender.process_response(user_input)
            st.session_state.display_history.append({
                "user_message": user_input,
                "recommendations": recommendations,
                "ai_prompt": next_prompt
            })
            st.session_state.current_prompt = next_prompt
            st.session_state.current_input_value = ""
    else:
        st.warning("Please provide a response.")

# Function to reset the conversation
def reset_conversation():
    st.session_state.recommender = CareerRecommender()
    st.session_state.display_history = []
    st.session_state.current_prompt = st.session_state.recommender.start_conversation()
    st.session_state.current_input_value = ""

# Main content area
st.title("AI-Powered Career Navigator")
st.markdown("### Your Personalized Journey to Professional Growth")

# Display conversation history
for turn in st.session_state.display_history:
    if "user_message" in turn:
        st.markdown(f"**You:** {turn['user_message']}")
    
    if "recommendations" in turn and turn['recommendations']:
        st.markdown("### Your Career Path Recommendations")
        for rec in turn['recommendations']:
            with st.expander(f"{rec['path']} - Confidence: {rec['confidence']:.0%}"):
                confidence_class = "confidence-high" if rec['confidence'] > 0.7 else "confidence-medium" if rec['confidence'] > 0.4 else "confidence-low"
                st.markdown(f"""
                    <div class="recommendation-box">
                        <h3>{rec['path']}<span class="confidence-badge {confidence_class}">{rec['confidence']:.0%}</span></h3>
                        <p><strong>Overview:</strong><br>{rec['description']}</p>
                        <p><strong>Recommended Career Options:</strong></p>
                        <ol>
                            {' '.join(f'<li>{career}</li>' for career in rec['careers'][:3])}
                        </ol>
                        <h4>Career Roadmap:</h4>
                        <ol>
                            {' '.join(f'<li>{step}</li>' for step in rec['roadmap'])}
                        </ol>
                    </div>
                """, unsafe_allow_html=True)
    
    if "ai_prompt" in turn:
        st.markdown(f"**AI:** {turn['ai_prompt']}")

# Display the current prompt
if not st.session_state.display_history:
    st.markdown("### Let's Begin")

st.markdown(st.session_state.current_prompt)

# Input section using st.form
with st.form(key='user_input_form'):
    user_response_label = "Share your interests, skills, and what you enjoy doing:" if not st.session_state.display_history else "Your response to the AI:"
    st.text_area(
        user_response_label,
        value=st.session_state.current_input_value,
        height=150,
        max_chars=1000,
        key="user_input_form_key"
    )
    
    submit_col, reset_col = st.columns([0.7, 0.3])
    with submit_col:
        st.form_submit_button("Submit", type="primary", on_click=handle_submit, use_container_width=True)
    with reset_col:
        st.form_submit_button("Reset Conversation", type="secondary", on_click=reset_conversation, use_container_width=True)

# Footer
st.markdown("""
    <footer>
        Built with ❤️ using Streamlit and Mistral AI | 
        <a href="https://github.com/your-repo" target="_blank">GitHub</a> | 
        <a href="https://streamlit.io" target="_blank">Streamlit</a>
    </footer>
""", unsafe_allow_html=True)
