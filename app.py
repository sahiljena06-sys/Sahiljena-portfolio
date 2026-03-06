import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Fetch the Groq API key from environment variables
api_key = os.environ.get("GROQ_API_KEY")

try:
    groq_client = Groq(api_key=api_key) if api_key else None
    if not groq_client:
        print("Warning: GROQ_API_KEY not found in environment variables.")
except Exception as e:
    groq_client = None
    print(f"Error initializing Groq client: {e}")

# Resume Data
resume_data = {
    "personal": {
        "name": "Sahil Jena",
        "title": "B.Tech Student | Front-End & Full Stack Enthusiast",
        "location": "Odisha, India",
        "email": "sahiljena06@gmail.com",
        "phone": "+91 78495 19700",
        "linkedin": "linkedin.com/in/sahiljena",
        "github": "sahiljena06-sys",
        "summary": "Motivated and detail-oriented 2nd year B.Tech student at NIST University with a strong foundation in front-end development and programming. Passionate about building efficient, user-friendly web applications and exploring full-stack development. Eager to apply technical skills and academic knowledge in a real-world internship environment."
    },
    "education": [
        {
            "degree": "Bachelor of Technology (B.Tech) \u2014 Computer Science & Engineering",
            "institution": "NIST University, Odisha, India",
            "duration": "2024 \u2013 2028",
            "details": [
                "2nd Year (Running) | Relevant coursework: Data Structures, OOP, Web Technologies, DBMS",
                "Actively participating in coding clubs and technology workshops"
            ]
        },
        {
            "degree": "Higher Secondary (12th) \u2014 Science Stream",
            "institution": "K.S.U.B College, Bhanjanagar, Odisha",
            "duration": "Pass Out: 2024",
            "details": []
        }
    ],
    "skills": {
        "Front-End Development": "HTML5, CSS3, JavaScript (ES6+)",
        "Programming Languages": "Python, C++",
        "Web Technologies": "Responsive Design, DOM Manipulation, REST APIs",
        "AI Tools": "GitHub Copilot, ChatGPT, Claude \u2014 for productivity & development",
        "Interests": "Full Stack Development, Open Source, UI/UX Design"
    },
    "projects": [
        {
            "name": "Full Stack Task Manager App",
            "tech": "Python \u00b7 Flask \u00b7 JavaScript \u00b7 SQLite",
            "link": "Personal Project",
            "bullets": [
                "Developed a full-stack web application with Python (Flask) backend and JavaScript frontend",
                "Implemented user authentication, CRUD operations, and a responsive UI using HTML/CSS",
                "Integrated SQLite database for persistent task storage and deployed on a local server"
            ]
        },
        {
            "name": "Personal Portfolio Website",
            "tech": "HTML \u00b7 CSS \u00b7 JavaScript",
            "link": "Personal Project | sahiljena.github.io",
            "bullets": [
                "Designed and deployed a responsive portfolio site showcasing projects, skills, and achievements",
                "Applied modern CSS techniques including Flexbox, Grid, and CSS animations"
            ]
        }
    ],
    "tools_tech": {
        "Version Control": "Git, GitHub",
        "IDE / Editors": "VS Code, PyCharm",
        "OS": "Windows, Linux (basic)",
        "Deployment": "GitHub Pages, Localhost"
    },
    "strengths": [
        {"name": "Fast Learner", "desc": "Quick to adapt to new frameworks and technologies with a growth mindset."},
        {"name": "Problem Solver", "desc": "Analytical approach to debugging and breaking down complex problems."},
        {"name": "Team Collaborator", "desc": "Comfortable working in teams through group projects and hackathons."},
        {"name": "Detail-Oriented", "desc": "Committed to delivering high-quality, detail-oriented results."}
    ]
}

SYSTEM_PROMPT = f"""You are a helpful AI assistant embedded in the personal portfolio website of Sahil Jena.
Your task is to answer questions about Sahil based ONLY on the following structured resume data:

{json.dumps(resume_data, indent=2)}

Guidelines:
- Answer accurately using the data provided.
- Keep answers concise (1-3 sentences max), friendly, and professional.
- Do not make up information. If you don't know something, tell them politely and suggest emailing sahiljena06@gmail.com.
- Format responses as plain text that looks good in a small chat widget context. Do not use complex markdown that requires a parser.
"""

@app.route('/')
def index():
    return render_template('index.html', d=resume_data)

@app.route('/chat', methods=['POST'])
def chat():
    if not groq_client:
        return jsonify({"response": "Chat service is temporarily unavailable due to API initialization errors."}), 500

    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            model="llama3-8b-8192", 
            temperature=0.4,
            max_tokens=250,
        )
        ai_response = chat_completion.choices[0].message.content
        return jsonify({"response": ai_response})
    
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return jsonify({"response": "Oops! I encountered an error trying to process your request. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
