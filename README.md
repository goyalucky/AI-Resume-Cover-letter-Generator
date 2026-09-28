AI-Resume-Cover-letter-Generator
An AI-powered web tool built with Python and Flask to generate tailored resumes and professional cover letters for job applications.
🚀 Features
Automated Document Generation: Creates tailored resumes and cover letters in seconds.
Job Matching: Aligns candidate experience with target job descriptions.
Clean Interface: Lightweight web UI rendered using Flask templates.
Customizable: Easily extendable to integrate with different LLM APIs (OpenAI, Gemini, Hugging Face, etc.).
📁 Repository Structure
AI-Resume-Cover-letter-Generator/
├── templates/          # HTML views and web frontend templates
├── .gitignore          # Standard Git ignore configuration
├── app.py              # Main Flask application backend and routing
├── requirements.txt    # Python dependencies needed to run the app
└── README.md           # Documentation


🛠️ Installation & Setup
1. Clone the repository
git clone https://github.com/goyalucky/AI-Resume-Cover-letter-Generator.git
cd AI-Resume-Cover-letter-Generator


2. Create and activate a virtual environment
Windows:
python -m venv venv
venv\Scripts\activate


macOS / Linux:
python3 -m venv venv
source venv/bin/activate


3. Install dependencies
pip install -r requirements.txt


4. Configure API Keys
Create a .env file in the project root directory and add your AI credentials:
OPENAI_API_KEY="your-api-key-here"
# or
GEMINI_API_KEY="your-api-key-here"


💻 Running the App
Start the Flask server:
python app.py


Access the application:
Open your browser and navigate to:
http://127.0.0.1:5000


📄 License
This project is licensed under the MIT License.
