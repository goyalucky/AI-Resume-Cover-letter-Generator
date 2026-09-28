# 🤖 AI Resume & Cover Letter Generator

An **AI-powered web application** built with **Python and Flask** that generates **tailored resumes and professional cover letters** based on a candidate's profile and target job description.

The application helps job seekers quickly customize their application documents by matching their **skills, experience, and qualifications** with the requirements of a specific job.

---

## 🚀 Features

* 📄 **Automated Resume Generation**
  Generate tailored resumes based on candidate information and job requirements.

* ✉️ **AI Cover Letter Generation**
  Create professional and job-specific cover letters in seconds.

* 🎯 **Job Description Matching**
  Analyzes the target job description and aligns the candidate's skills and experience with relevant requirements.

* 🤖 **LLM Integration Ready**
  Designed to work with AI/LLM APIs such as **OpenAI, Google Gemini, Hugging Face**, and other compatible providers.

* 🌐 **Clean Web Interface**
  Lightweight and user-friendly frontend built using **HTML/CSS and Flask templates**.

* ⚡ **Fast Document Generation**
  Automates repetitive resume and cover-letter writing tasks.

* 🔧 **Customizable Architecture**
  Easily extend the application with additional AI models, prompts, templates, and features.

---

## 🛠️ Tech Stack

| Technology              | Purpose                          |
| ----------------------- | -------------------------------- |
| 🐍 Python               | Backend development              |
| 🌐 Flask                | Web framework                    |
| 🤖 Generative AI / LLMs | Resume & cover-letter generation |
| 🎨 HTML/CSS             | Frontend interface               |
| 🔑 dotenv               | Environment variable management  |
| 🔗 REST APIs            | AI model integration             |

---

## 📁 Repository Structure

```text
AI-Resume-Cover-letter-Generator/
│
├── templates/
│   └── # HTML views and frontend templates
│
├── .gitignore
│
├── app.py
│   └── # Main Flask application and routing
│
├── requirements.txt
│   └── # Python dependencies
│
└── README.md
    └── # Project documentation
```

---

## ⚙️ How It Works

The application follows a simple AI-powered workflow:

```text
Candidate Information
        │
        ▼
Job Description
        │
        ▼
   Flask Backend
        │
        ▼
   AI / LLM API
        │
        ▼
Job-Specific Analysis
        │
        ├───────────────┐
        ▼               ▼
Tailored Resume   Cover Letter
        │               │
        └───────┬───────┘
                ▼
        Generated Output
```

### Workflow

1. 👤 Enter candidate information such as skills, experience, education, and projects.
2. 💼 Provide the target job description.
3. 🔍 The application identifies relevant skills and requirements.
4. 🤖 The information is processed using an integrated LLM.
5. 📄 A customized resume is generated.
6. ✉️ A professional cover letter is generated based on the same job requirements.

---

# 💻 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/goyalucky/AI-Resume-Cover-letter-Generator.git
cd AI-Resume-Cover-letter-Generator
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Keys

Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY="your-api-key-here"
```

Or, if using Google Gemini:

```env
GEMINI_API_KEY="your-api-key-here"
```

> ⚠️ **Important:** Never commit your `.env` file or expose your API keys publicly. Make sure `.env` is included in your `.gitignore`.

---

# ▶️ Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser to start using the application.

---

# 📸 Application Preview

Add screenshots of your application here to make the repository more attractive to recruiters.

```markdown
![Application Screenshot](path/to/screenshot.png)
```

You can also create a dedicated screenshots folder:

```text
screenshots/
├── home.png
├── resume-generation.png
└── cover-letter.png
```

Then use:

```markdown
![Home Page](screenshots/home.png)

![Resume Generation](screenshots/resume-generation.png)

![Cover Letter](screenshots/cover-letter.png)
```

---

# 🔮 Future Enhancements

Some potential improvements for future versions include:

* 📄 Export generated resumes as **PDF/DOCX**
* 🎯 ATS-friendly resume optimization
* 📊 Resume-job compatibility analysis
* 🔎 Keyword extraction from job descriptions
* 🧠 Improved prompt engineering and structured LLM output
* 📑 Multiple professional resume templates
* 🎨 Resume customization and formatting
* 🔐 User authentication
* 💾 Save and manage generated resumes
* 📧 Job application tracking
* 🤖 Support for additional LLM providers
* ☁️ Cloud deployment using platforms such as Render, Railway, or AWS

---

# 🔐 Security

API credentials should always be stored using environment variables.

Example:

```env
OPENAI_API_KEY="your-api-key"
GEMINI_API_KEY="your-api-key"
```

Do **not** hard-code API keys directly into Python source files.

Also ensure that `.env` is included in `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git add .
git commit -m "Add new feature"
```

5. Push the branch.

```bash
git push origin feature/your-feature
```

6. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Lucky Goyal**

🎓 AI/ML Undergraduate
💻 Python | Java | AI/ML | Generative AI | LLMs | RAG | Flask

### 🔗 Connect With Me

* 💼 LinkedIn: [https://www.linkedin.com/in/lucky-goyal-111766260/]
* 🐙 GitHub: https://github.com/goyalucky

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

Your support helps motivate further development and improvements. 🚀

---

### 💡 Project Highlights

> **AI-powered resume customization + job matching + automated cover letter generation — all through a lightweight Flask web application.**
