
SKILLS=[
"python","java","sql","machine learning","deep learning",
"aws","git","power bi","excel","data analysis",
"javascript","react","node","docker","kubernetes"
]

def get_skills(text):
    text=text.lower()
    return [s for s in SKILLS if s in text]
