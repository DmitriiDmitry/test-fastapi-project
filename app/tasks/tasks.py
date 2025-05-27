import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.tasks.celery_config import celery
from app.tasks.email_templates import creating_booking_confirmation_template


@celery.task
def process_pic(
        path: str
):
    image_path = Path(path)
    img = Image.open(image_path)
    img_resized_1000 = img.resize((1000, 500))
    img_resized_200 = img.resize((200, 100))
    img_resized_1000.save(f"app/static/images/resized_1000{image_path.name}")
    img_resized_200.save(f"app/static/images/resized_200{image_path.name}")


@celery.task
def send_confirm_email(
        booking: dict,
        email_to: EmailStr
):
    email_to_mock = settings.SMTP_USER
    msg_content = creating_booking_confirmation_template(booking, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
