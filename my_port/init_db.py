import sqlite3
import os
from flask import redirect,url_for

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DB_PATH = os.path.join(INSTANCE_DIR, "portfolio.db")


loc_i = "assets/icons/"
loc_t = "assets/thumbnails/"

socials = [
    # social media and contact information
    {
        "platform": "email",
        "url": "mailto:atulpachouri20@email.com",
        "icon": loc_i + "email.png"
    },
    {
        "platform": "linkedin",
        "url": "https://www.linkedin.com/in/atul-pachauri-data-analyst/",
        "icon": loc_i + "linkedin.png"
    },
    {
        "platform": "github",
        "url": "https://github.com/atulpachauri",
        "icon": loc_i + "github.png"
    },
]
# with app.test_request_context():

projects = [
    # personal GitHub projects to showcase
    {
        "title": "Flask App",
        "description": "Calculate different Type of numeric calculations",
        # "url": redirect(url_for("calculate_bp.home")),
        "url": "/calculate/",
        "thumbnail": loc_t + "voice_chat.png"
    },
    {
        "title": "Restaurant data analysis on user Engagement",
        "description": "How user engagement experience a corresponding increase in review and ratings",
        "url": "https://github.com/atulpachauri/SQL_Projects/blob/main/Restaurant_data_analysis.ipynb",
        "thumbnail": loc_t + "recipe_picker.png"
    },
    {
        "title": "Amazon sales Case Study",
        "description": "Analysis on different factors that affect sales of the different branches",
        "url": "https://github.com/atulpachauri/SQL_Projects/blob/main/SQL Project Amazon sales Case Study.pptx",
        "thumbnail": loc_t + "stock_prediction.png"
    },
    {
        "title": "Movie Recommender System",
        "description": "Movie recommender system a machine learning model recommends similar movies",
        "url": "https://github.com/atulpachauri/My_Projects/blob/main/Movie_Recommender_System.ipynb",
        "thumbnail": loc_t + "recomend.png"
    },
    {
        "title": "Online Retail Exploratory Data Analysis",
        "description": "Identifying most selling product across different country which can help to plan inventory stock",
        "url": "https://github.com/atulpachauri/My_Projects/blob/main/online_retail.ipynb",
        "thumbnail": loc_t + "dj_studio.png"
    },
    {
        "title": "Predictive Modeling",
        "description": "Identifying product defects based on historical data",
        "url": "https://github.com/atulpachauri/My_Projects/blob/main/Data manipulation and linear regression over iris dataset.ipynb",
        "thumbnail": loc_t + "image_gen.png"
    },
    {
        "title": "Diwali Sales Analysis",
        "description": "Identifying which product on which location are most saling product on Diwali",
        "url": "https://github.com/atulpachauri/My_Projects/blob/main/Python Diwali Sales Analysis Project .ipynb",
        "thumbnail": loc_t + "diwali.png"
    }
]

skills = [
    # software and tools showcased in the protfolio
    {"name": "Python"},
    {"name": "HTML"},
    {"name": "Docker"},
    {"name": "SQL"},
    {"name": "PowerBI"},
    {"name": "ETL(SSIS)"},
    {"name": "Flask"},
    {"name": "Git"},
    {"name": "PySpark"},
    {"name": "BigData"},
    {"name": "MongoDB"},
    {"name": "Machine Learning"},
    {"name": "Looker Studio"},
    {"name": "Google Cloud"},
]

profile = [
    {
        "name": "Atul Pachauri",
        "title": "Data Science Professional",
        "bio": "Data Science Certified, Passionate about Data and AI",
        "location": "Agra, Uttar Pradesh India"
    }
]


# # conn = get_db()
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS socials')
c.execute('DROP TABLE IF EXISTS projects')
c.execute('DROP TABLE IF EXISTS skills')
c.execute('DROP TABLE IF EXISTS profile')

c.execute('CREATE TABLE socials (id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, url TEXT, icon TEXT)')
c.execute('CREATE TABLE projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, url TEXT, thumbnail TEXT)')
c.execute('CREATE TABLE skills (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
c.execute('CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, bio TEXT, location TEXT)')

c.executemany('INSERT INTO socials (platform, url, icon) VALUES (:platform, :url, :icon)', socials)
c.executemany('INSERT INTO projects (title, description, url, thumbnail) VALUES (:title, :description, :url, :thumbnail)', projects)
c.executemany('INSERT INTO skills (name) VALUES (:name)', skills)
c.executemany('INSERT INTO profile (name, title, bio, location) VALUES (:name, :title, :bio, :location)', profile)

conn.commit()
conn.close()

print("Database tables dropped and repopulated in instance/portfolio.db!")

# step 1
# delete database

# step 2
# run this command to create new database
# python my_port/init_db.py     
# Database recreated successfully at: C:\Users\...\merged_app\instance\portfolio.db













