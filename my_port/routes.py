from flask import render_template, current_app
import sqlite3
import os
from . import port_bp

# --- DB CONNECTION ---
def get_db_connection():
    db_path = os.path.join(current_app.instance_path, "portfolio.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@port_bp.route("/")
def port_home():
    conn = get_db_connection()
    c = conn.cursor()

    socials = c.execute("SELECT * FROM socials").fetchall()
    projects = c.execute("SELECT * FROM projects").fetchall()
    skills = c.execute("SELECT * FROM skills").fetchall()
    profile = c.execute("SELECT * FROM profile").fetchone()

    conn.close()

    return render_template(
        "index.html",
        socials=socials,
        skills=skills,
        projects=projects,
        profile=profile
    )