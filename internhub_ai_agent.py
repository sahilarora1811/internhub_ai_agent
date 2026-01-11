def internship_ai_agent(profile, jd):
    matched_skills = set(profile["skills"]).intersection(jd["skills"])
    missing_skills = set(jd["skills"]) - set(profile["skills"])

    score = int((len(matched_skills) / len(jd["skills"])) * 100)

    result = {
        "Internship Match Summary":
            f"You match well with the internship based on skills like {', '.join(matched_skills)}.",

        "Skill Gap Explanation":
            f"You need to improve skills such as {', '.join(missing_skills)}.",

        "Recommendation":
            "Work on missing skills and build 1–2 relevant projects.",

        "ATS Confidence Score":
            f"{score}%"
    }

    return result


# Sample input
student_profile = {
    "name": "Sahil Arora",
    "skills": ["Python", "Machine Learning", "Pandas", "SQL"],
    "interests": ["AI", "Data Science"],
    "experience": "Built ML and Data Analysis projects"
}

internship_jd = {
    "role": "Data Science Intern",
    "skills": ["Python", "Machine Learning", "Deep Learning", "Data Analysis"]
}

# Run AI Agent
output = internship_ai_agent(student_profile, internship_jd)

for key, value in output.items():
    print(f"\n{key}:\n{value}")
