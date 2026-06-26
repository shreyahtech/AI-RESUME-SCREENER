
def generate_questions(jd):
    questions=[]

    if "python" in jd.lower():
        questions.append("Explain Python decorators.")
    if "sql" in jd.lower():
        questions.append("Difference between INNER and LEFT JOIN?")
    if "machine learning" in jd.lower():
        questions.append("Explain overfitting and underfitting.")

    questions.append("Describe a challenging project you worked on.")
    return questions
