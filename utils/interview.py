from utils.skills import get_skills


def generate_questions(jd, resume_skills):

    questions = []

    jd_skills = get_skills(jd)

    # Skills required by the JD that the candidate has
    common_skills = list(
        set(jd_skills).intersection(set(resume_skills))
    )

    # Technical questions
    question_bank = {
        "python": [
            "Explain Python decorators.",
            "What are generators in Python?",
            "Difference between a list and a tuple?"
        ],
        "sql": [
            "Difference between INNER JOIN and LEFT JOIN?",
            "How do indexes improve SQL performance?",
            "Explain normalization."
        ],
        "machine learning": [
            "Explain overfitting and underfitting.",
            "Difference between Bagging and Boosting.",
            "How would you evaluate a classification model?"
        ],
        "deep learning": [
            "Difference between CNNs and RNNs?",
            "What is backpropagation?"
        ],
        "tensorflow": [
            "How does TensorFlow handle tensors?",
            "Explain transfer learning."
        ],
        "pandas": [
            "Difference between loc and iloc.",
            "How do you handle missing values?"
        ],
        "numpy": [
            "Broadcasting in NumPy?",
            "Difference between reshape() and flatten()."
        ],
        "streamlit": [
            "Why did you choose Streamlit?",
            "How does Streamlit manage session state?"
        ],
        "docker": [
            "Difference between Docker images and containers.",
            "What are Docker volumes?"
        ],
        "aws": [
            "What AWS services have you used?",
            "Difference between EC2 and Lambda?"
        ],
        "react": [
            "Explain the Virtual DOM.",
            "What are React Hooks?"
        ],
        "node": [
            "Explain the event loop in Node.js.",
            "Difference between Express and Node?"
        ],
        "java": [
            "Explain JVM.",
            "Difference between Abstract Class and Interface?"
        ]
    }

    for skill in common_skills:

        key = skill.lower()

        if key in question_bank:
            questions.extend(question_bank[key])

    # Generic behavioural questions
    questions.extend([
        "Describe a challenging project you worked on.",
        "Tell me about a time you solved a difficult technical problem.",
        "How do you approach debugging a complex issue?"
    ])

    # Remove duplicates while preserving order
    seen = set()
    final_questions = []

    for q in questions:
        if q not in seen:
            seen.add(q)
            final_questions.append(q)

    return final_questions[:10]