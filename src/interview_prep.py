from datetime import datetime
import random

question = [
    "Tell me a little about yourself?",
    "What are your greatest strength and weakness?",
    "Why should we hire you?"
]

STRENGTH_OPT = [
    "strong problem-solving skills",
    "excellent communication skills",
    "ability to work well under pressure",
    "strong technical expertise in automation and web development",
    "leadership and team collaboration skills"
]

WEAKNESS_OPT = [
    "I can be overly detail-oriented, which can slow me down",
    "I sometimes take on too many responsibilities at once",
    "I may struggle with delegating tasks",
    "I tend to be too self-critical when projects don't go as planned",
    "I can get too focused on technical details and lose sight of the bigger picture"
]

# Fungsi untuk menjawab pertanyaan
def answer_question(cv):
    answer = {}
    retval = []
    
    name = cv["candidate_name"]
    latest_position = cv["positions"][0]
    education = cv["education_qualifications"][0]
    end_date_edu = datetime.strptime(education["end_date"], "%Y-%m-%d")
    position_desc = f"previously worked as a {latest_position['position_name']} at {latest_position['company_name']}"
    education_desc = f"{'graduated with' if end_date_edu < datetime.now() else 'pursuing'} a {education['degree_type']} in {education['faculty_department']} from {education['school_name']} with a decent GPA"
    strength = random.choice(STRENGTH_OPT)
    weakness = random.choice(WEAKNESS_OPT)
    latest_position = cv["positions"][0]

    answer[question[0]] = f"My name is {name}. I {position_desc}. I am {education_desc}."
    answer[question[1]] = f"My greatest strength is my {strength}. My weakness is that {weakness}"
    answer[question[2]] = (f"You should hire me because I have strong technical skills such as {', '.join(latest_position['skills'][:3])}. "
                          f"In my role at {latest_position['company_name']}, I also successfully {latest_position['job_details']}")

    for key, value in answer.items():
        retval.append({"question" : key, "bestAnswer": value})
    
    return retval

