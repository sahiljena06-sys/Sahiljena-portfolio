# Dashboard Portfolio Website with AI Chatbot

A simple, colorful, modern, and unscrollable dashboard-style portfolio website built using Python (Flask), HTML, and CSS. This portfolio includes a minimizable AI chatbot powered by the Groq API (`llama3-8b-8192` model) that acts as an intelligent assistant, answering questions using structured resume data.

## Features
- **Dashboard Layout**: Single-screen, clean overview of Education, Skills, Projects, and Tools.
- **Modern Aesthetics**: Glassmorphism, dark-mode gradient UI, unscrollable layout (`100vh`), and micro-animations.
- **AI Assistant**: Floating chat widget integrated with Groq API for lightning-fast, contextual responses about Sahil's background.

## Local Development Setup

To run this application locally, follow these steps:

1. **Clone or Download the Repository**
2. **Setup virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables**
   The application uses a `.env` file to manage the API key securely. An example of the `.env` file structure is included. Make sure your `.env` contains your API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
5. **Run the Application**
   ```bash
   python app.py
   ```
   The site will be available at `http://127.0.0.1:5000/`.

## Deployment to Render

This application is configured for easy deployment on [Render](https://render.com/).

### Steps to Deploy:
1. Push this project folder to a **GitHub Repository**.
2. Log in to Render and click **New > Web Service**.
3. Connect your GitHub account and select the repository.
4. Render will try to autodetect settings. Configure them as follows:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (This uses the included `Procfile` / explicitly runs via Gunicorn)
5. **Environment Variables on Render:**
   - Under the "Environment" tab of your deployment settings, add the variable:
     - **Key:** `GROQ_API_KEY`
     - **Value:** `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` (or your preferred Groq Key)
6. Click **Create Web Service**. Render will build and deploy the application. Once complete, you will get a live `.onrender.com` URL.
