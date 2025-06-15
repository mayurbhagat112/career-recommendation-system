from typing import Dict, List, Tuple

CAREER_PATHS = {
    "STEM": {
        "keywords": ["science", "technology", "engineering", "math", "programming", "data", "research", "analysis", "ai", "machine learning", "robotics", "cybersecurity"],
        "careers": [
            "Software Engineer",
            "Data Scientist",
            "Research Scientist",
            "Mechanical Engineer",
            "Electrical Engineer",
            "Civil Engineer",
            "Data Analyst",
            "AI/ML Engineer",
            "Cybersecurity Specialist",
            "Robotics Engineer"
        ],
        "description": "STEM careers focus on science, technology, engineering, and mathematics. These roles typically involve problem-solving, analytical thinking, and innovation.",
        "roadmap": [
            "Foundation (Strong Math, Programming Basics)",
            "Entry-Level (e.g., Junior Developer, Data Analyst)",
            "Mid-Level (e.g., Software Engineer, Data Scientist)",
            "Senior/Lead (e.g., Senior Engineer, AI/ML Lead, Research Lead)",
            "Specialization/Management (e.g., Architect, CTO, Principal Scientist)"
        ]
    },
    "Arts": {
        "keywords": ["art", "design", "creativity", "music", "writing", "media", "visual", "performance", "photography", "film", "theater"],
        "careers": [
            "Graphic Designer",
            "UX/UI Designer",
            "Content Writer",
            "Digital Artist",
            "Music Producer",
            "Art Director",
            "Architect",
            "Fashion Designer",
            "Photographer",
            "Filmmaker",
            "Theater Director"
        ],
        "description": "Arts careers emphasize creativity, design, and expression. These roles often combine technical skills with artistic vision.",
        "roadmap": [
            "Foundation (Portfolio Building, Fundamental Skills)",
            "Entry-Level (e.g., Junior Designer, Production Assistant)",
            "Mid-Level (e.g., Lead Artist, Senior Writer)",
            "Senior/Creative Lead (e.g., Creative Director, Art Director)",
            "Freelance/Entrepreneurship (Establishing own studio/brand)"
        ]
    },
    "Business": {
        "keywords": ["business", "management", "finance", "marketing", "sales", "entrepreneurship", "strategy", "consulting", "real estate", "logistics"],
        "careers": [
            "Business Analyst",
            "Marketing Manager",
            "Financial Analyst",
            "Project Manager",
            "Entrepreneur",
            "Management Consultant",
            "Sales Manager",
            "HR Manager",
            "Real Estate Agent",
            "Logistics Coordinator",
            "Consultant"
        ],
        "description": "Business careers focus on organizational management, strategy, and operations. These roles require strong leadership and analytical skills.",
        "roadmap": [
            "Foundation (Business Acumen, Communication Skills)",
            "Entry-Level (e.g., Analyst, Coordinator)",
            "Mid-Level (e.g., Manager, Senior Consultant)",
            "Senior/Director (e.g., Director of Operations, Head of Marketing)",
            "Executive Leadership (e.g., CEO, CFO, VP)"
        ]
    },
    "Healthcare": {
        "keywords": ["health", "medical", "care", "wellness", "therapy", "nursing", "pharmacy", "dentistry", "veterinary", "nutrition"],
        "careers": [
            "Medical Doctor",
            "Nurse",
            "Physical Therapist",
            "Pharmacist",
            "Mental Health Professional",
            "Healthcare Administrator",
            "Medical Researcher",
            "Public Health Specialist",
            "Dentist",
            "Veterinarian",
            "Nutritionist"
        ],
        "description": "Healthcare careers involve patient care, medical research, and health services. These roles require strong interpersonal skills and scientific knowledge.",
        "roadmap": [
            "Foundation (Pre-med, Nursing School, Health Sciences)",
            "Entry-Level (e.g., Registered Nurse, Medical Assistant)",
            "Mid-Level (e.g., Specialist Doctor, Nurse Practitioner)",
            "Senior/Leadership (e.g., Chief of Staff, Hospital Administrator)",
            "Advanced Practice/Research (e.g., Surgeon, Medical Researcher)"
        ]
    },
    "Education": {
        "keywords": ["teaching", "education", "learning", "training", "mentoring", "curriculum", "e-learning", "instructional design"],
        "careers": [
            "Teacher",
            "Educational Administrator",
            "Curriculum Developer",
            "Educational Consultant",
            "Special Education Teacher",
            "School Counselor",
            "Professor",
            "Corporate Trainer",
            "Instructional Designer",
            "E-learning Specialist"
        ],
        "description": "Education careers focus on teaching, training, and developing others. These roles require strong communication and organizational skills.",
        "roadmap": [
            "Foundation (Education Degree, Teaching Credential)",
            "Entry-Level (e.g., Classroom Teacher, Teaching Assistant)",
            "Mid-Level (e.g., Department Head, Lead Teacher)",
            "Leadership/Administration (e.g., Principal, Dean)",
            "Policy/Research (e.g., Educational Policy Maker, University Professor)"
        ]
    },
    "Sports": {
        "keywords": ["sports", "athletics", "fitness", "coaching", "training", "physical", "exercise", "competition", "sports medicine", "referee", "sports analytics"],
        "careers": [
            "Professional Athlete",
            "Sports Coach",
            "Fitness Trainer",
            "Physical Therapist",
            "Sports Psychologist",
            "Athletic Trainer",
            "Sports Journalist",
            "Sports Manager",
            "Sports Medicine Specialist",
            "Referee",
            "Sports Analyst"
        ],
        "description": "Sports careers involve physical activity, coaching, training, and sports management. These roles require physical fitness, teamwork, and leadership skills.",
        "roadmap": [
            "Foundation (Physical Fitness, Basic Training)",
            "Entry-Level (e.g., Assistant Coach, Fitness Instructor)",
            "Mid-Level (e.g., Coach, Athletic Trainer)",
            "Senior/Leadership (e.g., Head Coach, Sports Manager)",
            "Specialization/Entrepreneurship (e.g., Sports Agent, Personal Trainer Business Owner)"
        ]
    }
}

def map_interests_to_careers(interests: List[str]) -> List[Tuple[str, float]]:
    """
    Maps a list of interests to potential career paths with confidence scores.
    Returns a list of tuples (career_path, confidence_score).
    """
    scores = {path: 0 for path in CAREER_PATHS.keys()}
    
    for interest in interests:
        interest = interest.lower()
        for path, data in CAREER_PATHS.items():
            for keyword in data["keywords"]:
                if keyword in interest:
                    scores[path] += 1
    
    # Normalize scores
    total_matches = sum(scores.values())
    if total_matches > 0:
        scores = {path: score/total_matches for path, score in scores.items()}
    
    # Sort by confidence score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def get_career_description(path: str) -> str:
    """Returns the description for a given career path."""
    return CAREER_PATHS.get(path, {}).get("description", "No description available.")

def get_career_options(path: str) -> List[str]:
    """Returns the list of career options for a given path."""
    return CAREER_PATHS.get(path, {}).get("careers", [])

def get_career_roadmap(path: str) -> List[str]:
    """Returns the roadmap for a given career path."""
    return CAREER_PATHS.get(path, {}).get("roadmap", []) 