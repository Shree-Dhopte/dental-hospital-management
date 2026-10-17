# BrightSmile Dental Hospital — Python Backend Starter

This project includes:
- Responsive dental clinic website
- Flask Python backend
- SQLite database for storing appointment requests (zero database setup required)
- Appointment form validation and server-side storage
- Demo appointment request list at `/admin/appointments`
- Health check endpoint at `/health`
- Structure ready for future AI APIs

## Run locally (Windows)

1. Install Python 3.10+.
2. Extract this folder and open it in VS Code.
3. Open Terminal in this folder and run:

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

If `py` does not work, try `python` instead.

## Where the booking data is saved
A `dental_hospital.db` file is created automatically in this project folder. You can inspect appointments using the `/admin/appointments` page while the local server is running.

## Important limitations before real deployment
- The admin appointments page has no login. Do not expose it publicly until authentication and authorization are implemented.
- Appointment requests are stored as `Pending`; no email/SMS is sent, no calendar slot is reserved, and double-booking is not prevented.
- Replace demo clinic contact details and testimonials.
- For production, use a production WSGI server, environment-based secret key, HTTPS, CSRF protection, rate limiting, proper logging, backups, and privacy/security controls appropriate for patient data.
- SQLite is suitable for a small local prototype. MySQL can be introduced later by replacing the database access layer.

## Future AI integration
Keep future AI functionality in a separate module (for example `ai_services/`) and expose it through Flask routes. Potential features could include an FAQ chatbot or appointment assistant. Any dental image analysis or symptom-related AI must be clinically validated, privacy-protected, and clearly presented as supportive rather than a diagnosis.
