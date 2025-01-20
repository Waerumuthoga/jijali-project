#Jijali: A Self-Reflective Journal for Mental Wellbeing

**Jijali** is a self-reflective web application designed to help users journal, track their mood, and manage mental crises in a healthy, introspective way. The app provides users with a space to reflect on their emotions, understand the causes of their feelings, and cope with mental health challenges. Whether you're seeking to enhance your emotional awareness or need immediate support, Jijali offers tools to promote mental clarity and emotional wellbeing.
**Features**

    Daily Reflection Journal: Users can reflect on their day by journaling about their experiences and emotions.
    Mood and Emotion Tracking: Track various moods and emotions throughout the day and their underlying causes.
    Safe Venting Space: A secure space for users to vent their frustrations and share feelings freely.
    Crisis Support: Provides immediate tips and resources for users facing mental health crises, including links to helplines or self-help techniques.
    Supplementary Tool for Therapy: Ideal for those already in therapy or individuals looking for extra tools for emotional support.

**Technologies Used**

    Backend: Python, FastAPI
    Database: PostgreSQL
    Frontend: HTML, CSS, JavaScript
    Database Migrations: Alembic
    Authentication & Security: bcrypt, passlib, PyJWT
    API Documentation: FastAPI auto-generated docs
    Environment Management: Python-dotenv

**Getting Started**

To run this project locally, follow these steps:
**1. Clone the Repository**

https://github.com/Waerumuthoga/jijali-project
cd jijali

**2. Set Up a Virtual Environment**

It's recommended to create a virtual environment to manage dependencies.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**3. Install Dependencies**

Make sure you have pip installed, then run:

pip install -r requirements.txt

**4. Set Up the Database**

You'll need PostgreSQL installed locally or use a remote database service. Configure your database connection in the .env file. Make sure to set up environment variables for your database credentials.

Then, use Alembic to run database migrations:

alembic upgrade head

**5. Run the Application**

uvicorn app.main:app --reload

This will start the FastAPI server on http://localhost:8000.
6. Access the App

Navigate to http://localhost:8000 in your web browser to access the app.
