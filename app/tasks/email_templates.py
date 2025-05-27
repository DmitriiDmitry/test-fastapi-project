from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def creating_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()
    email["Subject"] = "Booking Confirmation"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Booking Confirmation</h1>
            You have booked the hotel from {booking['date_from']} until {booking['date_to']}
        
        """,
        subtype="html"
    )
    return email
