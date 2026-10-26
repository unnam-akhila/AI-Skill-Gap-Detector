from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample skills required for each job role
job_skills = {
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Python Developer": ["Python", "OOP", "SQL", "Flask", "Git"]
}


@app.route("/")
def home():
    return jsonify({
        "message": "AI Skill Gap Detector backend is running!"
    })


@app.route("/analyze", methods=["POST"])
def analyze_skills():
    data = request.get_json()

    role = data.get("role", "")
    user_skills = data.get("skills", [])

    if isinstance(user_skills, str):
        user_skills = user_skills.split(",")

    user_skills = [
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    ]

    if role not in job_skills:
        return jsonify({
            "error": "Please select a valid job role."
        }), 400

    required_skills = job_skills[role]

    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in user_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in user_skills
    ]

    return jsonify({
        "role": role,
        "current_skills": user_skills,
        "matched_skills": matched_skills,

        
        "missing_skills": missing_skills,
        "recommended_skills": missing_skills,
        "message": "Skill gap analysis completed successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)