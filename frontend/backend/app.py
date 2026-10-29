from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Skills required for 25 job roles
job_skills = {
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Python Developer": ["Python", "OOP", "SQL", "Flask", "Git"],
    "AI Engineer": ["Python", "Machine Learning", "SQL", "Statistics", "Deep Learning"],
    "Machine Learning Engineer": ["Python", "Statistics", "Machine Learning", "Scikit-learn", "Deep Learning"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Responsive Design"],
    "Backend Developer": ["Python", "Flask", "SQL", "REST API", "Git"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "React", "Flask", "SQL"],
    "Java Developer": ["Java", "OOP", "SQL", "Spring Boot", "Git"],
    "Software Engineer": ["Programming", "OOP", "Data Structures", "Git", "Testing"],
    "Software Tester": ["Manual Testing", "Test Cases", "SQL", "Selenium", "Bug Reporting"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Python", "Security Fundamentals", "SIEM"],
    "Cloud Engineer": ["Linux", "Networking", "AWS", "Docker", "Cloud Security"],
    "DevOps Engineer": ["Linux", "Git", "Docker", "CI/CD", "Cloud Computing"],
    "Database Administrator": ["SQL", "Database Design", "Backup and Recovery", "Indexing", "Database Security"],
    "Business Analyst": ["Requirements Analysis", "Excel", "SQL", "Data Visualization", "Communication"],
    "UI/UX Designer": ["User Research", "Wireframing", "Figma", "Prototyping", "Usability Testing"],
    "Mobile App Developer": ["Programming", "Mobile UI", "REST API", "Git", "Testing"],
    "Android Developer": ["Kotlin", "Java", "Android Studio", "REST API", "SQLite"],
    "Product Manager": ["Market Research", "Product Roadmapping", "Agile", "Data Analysis", "Communication"],
    "Digital Marketing Specialist": ["SEO", "Content Marketing", "Social Media", "Google Analytics", "Email Marketing"],
    "Network Engineer": ["Networking", "TCP/IP", "Routing and Switching", "Linux", "Network Security"],
    "Data Engineer": ["Python", "SQL", "ETL", "Data Warehousing", "Apache Spark"],
    "IT Support Specialist": ["Troubleshooting", "Windows", "Networking", "Hardware Support", "Cybersecurity Basics"]
}

# Learning topics and practical tasks for common skills
skill_guidance = {
    "Python": {
        "topics": ["Variables and data types", "Conditions and loops", "Functions and lists"],
        "task": "Write a Python program that accepts input and calculates a result."
    },
    "SQL": {
        "topics": ["SELECT queries", "WHERE and ORDER BY", "JOIN and GROUP BY"],
        "task": "Create a sample database and write five queries to retrieve information."
    },
    "Excel": {
        "topics": ["Formulas and functions", "Sorting and filtering", "Pivot tables and charts"],
        "task": "Create a spreadsheet and summarize sample data using a pivot table."
    },
    "Power BI": {
        "topics": ["Importing data", "Creating charts", "Building interactive dashboards"],
        "task": "Build a dashboard using a sample sales or student dataset."
    },
    "Statistics": {
        "topics": ["Mean, median and mode", "Probability", "Correlation and distributions"],
        "task": "Analyze a small dataset and explain its average and trends."
    },
    "HTML": {
        "topics": ["HTML structure", "Forms and input fields", "Semantic elements"],
        "task": "Build a simple webpage containing a heading, form and navigation."
    },
    "CSS": {
        "topics": ["Selectors and box model", "Flexbox and Grid", "Responsive design"],
        "task": "Style a webpage and make it work on mobile and desktop."
    },
    "JavaScript": {
        "topics": ["Variables and functions", "Arrays and objects", "DOM and events"],
        "task": "Build an interactive webpage with a button and form validation."
    },
    "React": {
        "topics": ["Components and JSX", "Props and state", "Hooks and API calls"],
        "task": "Create a React app that displays and filters a list of items."
    },
    "Git": {
        "topics": ["Repositories and commits", "Branches", "Push and pull"],
        "task": "Create a Git repository and commit a small project."
    },
    "OOP": {
        "topics": ["Classes and objects", "Inheritance", "Encapsulation"],
        "task": "Create a class-based program that models a real-world object."
    },
    "Flask": {
        "topics": ["Routes and HTTP methods", "Request and JSON handling", "REST APIs"],
        "task": "Build a Flask API with one GET route and one POST route."
    },
    "Machine Learning": {
        "topics": ["Supervised and unsupervised learning", "Training and testing data", "Model evaluation"],
        "task": "Train a beginner-friendly classification model using a sample dataset."
    },
    "Deep Learning": {
        "topics": ["Neural network basics", "Layers and activation functions", "Training a model"],
        "task": "Build a small neural network using a beginner tutorial and sample dataset."
    },
    "Scikit-learn": {
        "topics": ["Preparing datasets", "Training models", "Evaluating predictions"],
        "task": "Train a simple Scikit-learn model and measure its accuracy."
    },
    "Data Visualization": {
        "topics": ["Choosing chart types", "Comparing trends", "Communicating insights"],
        "task": "Create three charts from a dataset and explain what they show."
    },
    "Responsive Design": {
        "topics": ["Media queries", "Flexible layouts", "Mobile-first design"],
        "task": "Make a webpage adjust correctly to mobile, tablet and desktop sizes."
    },
    "REST API": {
        "topics": ["HTTP methods", "JSON requests and responses", "API error handling"],
        "task": "Build or test an API endpoint that accepts and returns JSON."
    },
    "Java": {
        "topics": ["Java syntax", "Classes and objects", "Collections and exceptions"],
        "task": "Build a small Java application using classes and collections."
    },
    "Programming": {
        "topics": ["Variables and data types", "Conditions and loops", "Functions"],
        "task": "Solve five beginner programming problems using your chosen language."
    },
    "Data Structures": {
        "topics": ["Arrays and linked lists", "Stacks and queues", "Searching and sorting"],
        "task": "Implement a stack and a basic searching algorithm."
    },
    "Manual Testing": {
        "topics": ["Testing fundamentals", "Positive and negative test cases", "Defect lifecycle"],
        "task": "Test a login form and document the results."
    },
    "Test Cases": {
        "topics": ["Test case structure", "Expected versus actual results", "Edge cases"],
        "task": "Write ten test cases for a registration form."
    },
    "Selenium": {
        "topics": ["Browser automation", "Locators", "Automated test scripts"],
        "task": "Automate a simple browser test using Selenium."
    },
    "Networking": {
        "topics": ["IP addresses", "DNS and DHCP", "Network troubleshooting"],
        "task": "Draw a small network diagram and practice basic connectivity commands."
    },
    "Linux": {
        "topics": ["Terminal commands", "Files and permissions", "Processes and services"],
        "task": "Practice creating files, navigating folders and checking running processes."
    },
    "Security Fundamentals": {
        "topics": ["Common security threats", "Authentication and authorization", "Security best practices"],
        "task": "Review a sample application and list basic security improvements."
    },
    "AWS": {
        "topics": ["Cloud computing basics", "Compute and storage services", "Identity and access management"],
        "task": "Complete a beginner cloud tutorial and deploy a simple sample application."
    },
    "Docker": {
        "topics": ["Images and containers", "Dockerfiles", "Container networking"],
        "task": "Containerize a small application using a basic Dockerfile."
    },
    "CI/CD": {
        "topics": ["Build and test automation", "Pipeline stages", "Deployment workflows"],
        "task": "Create a simple workflow that runs tests when code is pushed."
    },
    "Database Design": {
        "topics": ["Tables and relationships", "Primary and foreign keys", "Normalization"],
        "task": "Design a database schema for a student management system."
    },
    "User Research": {
        "topics": ["Identifying user needs", "Interviews and surveys", "Analyzing feedback"],
        "task": "Collect feedback from three users and summarize their needs."
    },
    "Figma": {
        "topics": ["Frames and components", "Auto layout", "Interactive prototypes"],
        "task": "Design a simple login screen and create a clickable prototype."
    },
    "SEO": {
        "topics": ["Keyword research", "On-page SEO", "Search performance"],
        "task": "Optimize a sample webpage title, headings and description."
    },
    "Communication": {
        "topics": ["Clear written communication", "Presenting ideas", "Active listening"],
        "task": "Prepare a short presentation explaining a project to a beginner."
    }
}


def get_guidance(skill):
    # Use specific guidance when available; otherwise provide a general plan.
    if skill in skill_guidance:
        return skill_guidance[skill]

    return {
        "topics": [
            f"{skill} fundamentals",
            f"Important tools and concepts in {skill}",
            f"Practical applications of {skill}"
        ],
        "task": f"Complete a beginner project that demonstrates your understanding of {skill}."
    }


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Skill Gap Detector backend is running!"
    })


@app.route("/roles", methods=["GET"])
def get_roles():
    return jsonify({
        "roles": list(job_skills.keys())
    })


@app.route("/analyze", methods=["POST"])
def analyze_skills():
    data = request.get_json(silent=True) or {}

    role = data.get("role", "").strip()
    user_skills = data.get("skills", [])

    if isinstance(user_skills, str):
        user_skills = user_skills.split(",")

    if not isinstance(user_skills, list):
        return jsonify({"error": "Skills must be a list or comma-separated text."}), 400

    user_skills = [
        str(skill).strip().lower()
        for skill in user_skills
        if str(skill).strip()
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

    match_percentage = round(
        (len(matched_skills) / len(required_skills)) * 100
    ) if required_skills else 0

    roadmap = []

    for skill in missing_skills:
        guidance = get_guidance(skill)
        roadmap.append({
            "skill": skill,
            "topics": guidance["topics"],
            "task": guidance["task"]
        })

    return jsonify({
        "role": role,
        "current_skills": user_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommended_skills": missing_skills,
        "match_percentage": match_percentage,
        "roadmap": roadmap,
        "message": "Skill gap analysis completed successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)