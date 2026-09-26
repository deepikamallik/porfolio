from flask import Flask, request, render_template
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__)

MY_EMAIL = "deepikamallik1006@gmail.com"
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send-message", methods=["POST"])
def send_message():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio Contact - Message from {name}"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg["Reply-To"] = email

    msg.set_content(
        f"""You received a new message from your portfolio.

Name: {name}
Email: {email}

Message:
{message}
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(MY_EMAIL, APP_PASSWORD)
            server.send_message(msg)

        return """
        <h2>Message sent successfully! ✅</h2>
        <p>Thank you for contacting me.</p>
        <a href="/">Go Back</a>
        """

    except Exception as e:
        return f"""
        <h2>Failed to send message ❌</h2>
        <p>{e}</p>
        <a href="/">Go Back</a>
        """


if __name__ == "__main__":
    app.run(debug=True)