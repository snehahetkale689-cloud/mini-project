from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Career Technical Skills
career_skills = {
    "web developer": ["html", "css", "javascript", "python","mysql","react","git"],
    "data analyst": ["python", "excel", "sql", "statistics"],
    "software developer": ["c++", "dsa", "oop", "git","python","php"],
    "backend developer": ["python", "java", "express.js(node.js)", "sql", "git", "api development"],
    "cyber security analyst": ["network security", "ethical hacking", "linux", "cryptography", "python"],
    "mobile app developer": ["java", "kotlin", "flutter", "android studio", "firebase"],
    "frontend developer": ["html", "css", "javascript", "react", "bootstrap"],
    "machine learning engineer": ["python", "machine learning", "tensorflow", "pandas", "numpy"],
    "full stack developer": ["html", "css", "javascript", "node.js", "mongodb"],
    "cloud engineer": ["aws", "azure", "linux", "docker", "networking"],
    "devops engineer": ["docker", "kubernetes", "jenkins", "linux", "git"],
    "ai engineer": ["python", "deep learning", "tensorflow", "nlp", "data science"],
    "network engineer": ["networking", "cisco", "tcp/ip", "firewall", "linux"]
}

# Career Soft Skills
soft_skills_data = {
    "web developer": ["Communication", "Problem Solving", "Teamwork", "Time Management"],
    "data analyst": ["Analytical Thinking", "Attention to Detail", "Presentation Skills"],
    "software developer": ["Logical Thinking", "Teamwork", "Adaptability"],
    "backend developer": ["Logical Thinking", "Teamwork", "Communication", "Problem Solving"],
    "cyber security analyst": ["Critical Thinking", "Attention to Detail", "Problem Solving", "Decision Making"],
    "mobile app developer": ["Creativity", "Problem Solving", "Teamwork", "Time Management"],
    "frontend developer": ["Creativity", "Communication", "Attention to Detail", "Teamwork"],
    "machine learning engineer": ["Analytical Thinking", "Problem Solving", "Research Skills", "Patience"],
    "full stack developer": ["Problem Solving", "Time Management", "Communication", "Teamwork"],
    "cloud engineer": ["Problem Solving", "Critical Thinking", "Collaboration", "Adaptability"],
    "devops engineer": ["Teamwork", "Communication", "Problem Solving", "Time Management"],
    "ai engineer": ["Analytical Thinking", "Research Skills", "Problem Solving", "Creativity"],
    "network engineer": ["Problem Solving", "Attention to Detail", "Communication", "Decision Making"]
}

# Home Page
@app.route('/')
def home():
   return render_template("index.html")

# Analyze Skills
@app.route('/analyze', methods=['POST'])
def analyze():

    name = request.form['name']
    career = request.form['career']
    skills = request.form['skills']

    # Convert user skills into list
    user_skills = [s.strip().lower() for s in skills.split(",")]

    # ---------- C++ PROGRAM ----------
    process_cpp = subprocess.Popen(
        ["user_data.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    process_cpp.communicate(f"{name}\n{career}\n{skills}")

    # ---------- TECHNICAL SKILLS ----------
    required_skills = career_skills.get(career.lower(), [])
    have=list(set(user_skills)& set(required_skills))

    match = len(set(user_skills) & set(required_skills))
    total = len(required_skills)
    

    # ---------- C PROGRAM ----------
    process_c = subprocess.Popen(
        ["calculate.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    percentage, _ = process_c.communicate(f"{total} {match}")
    percentage = percentage.strip()

    # Missing skills
    missing = list(set(required_skills) - set(user_skills))

    # ---------- SOFT SKILLS ----------
    soft_skills = soft_skills_data.get(career.lower(), [])

    return render_template(
        "result.html",
        name=name,
        career=career,
        percentage=percentage,
        user_skills=have,
        missing=missing,
        soft_skills=soft_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
