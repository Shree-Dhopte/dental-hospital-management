
from pathlib import Path
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "change-this-before-deployment"

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "dental_hospital.db"


def init_db():
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                service TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                message TEXT,
                status TEXT DEFAULT 'Pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book_appointment():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    appointment_date = request.form.get("date", "").strip()
    appointment_time = request.form.get("time", "").strip()
    message = request.form.get("message", "").strip()

    if not all([name, phone, service, appointment_date, appointment_time]):
        flash("Please complete all required fields.", "error")
        return redirect(url_for("home") + "#booking")

    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            INSERT INTO appointments
            (name, phone, email, service, appointment_date,
             appointment_time, message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, phone, email, service, appointment_date,
              appointment_time, message))

    flash("Appointment request submitted! The clinic must confirm it.",
          "success")
    return redirect(url_for("home") + "#booking")


@app.route("/admin/appointments")
def admin_appointments():
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory = sqlite3.Row
        appointments = db.execute(
            "SELECT * FROM appointments ORDER BY id DESC"
        ).fetchall()

    return render_template("admin.html", appointments=appointments)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
