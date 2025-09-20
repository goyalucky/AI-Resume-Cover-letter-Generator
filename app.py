from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
from datetime import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

app = Flask(__name__)
CORS(app)

def query_groq_model(prompt):
    """Call the GROQ API to get model response."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error from GROQ API: {response.status_code} - {response.text}"

class ResumeGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=20,
            spaceAfter=30,
            alignment=1  # Center
        ))
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            textColor=colors.darkblue,
        ))

    def generate_resume_content(self, user_data, job_description, tone='professional'):
        prompt = f"""
Generate a professional resume based on the following information:

Personal Information:
- Name: {user_data.get('name', '')}
- Email: {user_data.get('email', '')}
- Phone: {user_data.get('phone', '')}
- Location: {user_data.get('location', '')}

Experience: {user_data.get('experience', '')}
Education: {user_data.get('education', '')}
Skills: {user_data.get('skills', '')}

Job Description: {job_description}

Tone: {tone}

Please generate a well-structured resume with:
1. Professional summary (2-3 sentences)
2. Work experience with bullet points
3. Education section
4. Skills section
5. Make it ATS-friendly and keyword-optimized

Format the response in readable text, use line breaks to separate sections.
"""
        return query_groq_model(prompt)

    def generate_cover_letter(self, user_data, job_description, company_name, tone='professional'):
        prompt = f"""
Generate a personalized cover letter based on:

Personal Information:
- Name: {user_data.get('name', '')}
- Experience: {user_data.get('experience', '')}
- Skills: {user_data.get('skills', '')}

Job Description: {job_description}
Company: {company_name}
Tone: {tone}

Create a compelling cover letter that:
1. Addresses the specific job requirements
2. Highlights relevant experience and skills
3. Shows enthusiasm for the company
4. Includes a strong opening and closing
5. Matches the specified tone

Keep it professional and around 300-400 words.
"""
        return query_groq_model(prompt)

    def create_pdf_resume(self, user_data, resume_content):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        story = []

        # Title
        title = Paragraph(user_data.get('name', 'Resume'), self.styles['CustomTitle'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Contact Info
        contact_info = f"{user_data.get('email', '')} | {user_data.get('phone', '')} | {user_data.get('location', '')}"
        contact = Paragraph(contact_info, self.styles['Normal'])
        story.append(contact)
        story.append(Spacer(1, 20))

        # Resume content
        content_paragraph = Paragraph(resume_content.replace('\n', '<br/>'), self.styles['Normal'])
        story.append(content_paragraph)

        doc.build(story)
        buffer.seek(0)
        return buffer

resume_gen = ResumeGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    try:
        data = request.get_json()
        user_data = data.get('user_data', {})
        job_description = data.get('job_description', '')
        tone = data.get('tone', 'professional')

        resume_content = resume_gen.generate_resume_content(user_data, job_description, tone)

        return jsonify({
            'success': True,
            'resume_content': resume_content
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    try:
        data = request.get_json()
        user_data = data.get('user_data', {})
        job_description = data.get('job_description', '')
        company_name = data.get('company_name', '')
        tone = data.get('tone', 'professional')

        cover_letter = resume_gen.generate_cover_letter(user_data, job_description, company_name, tone)

        return jsonify({
            'success': True,
            'cover_letter': cover_letter
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    try:
        data = request.get_json()
        user_data = data.get('user_data', {})
        content = data.get('content', '')

        pdf_buffer = resume_gen.create_pdf_resume(user_data, content)

        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
