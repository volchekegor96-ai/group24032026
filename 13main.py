import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from pywebio import start_server
from pywebio.input import input_group, input, TEXT
from pywebio.output import put_text, put_success, put_error

SMTP_SERVER = "smtp.ukr.net"
SMTP_PORT = 1
SENDER_EMAIL = "volchekegor@ukr.net"
SENDER_TOKEN = "ZhtOava6wJ9rVsCx"


def render_email_body(template_name, context):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_name)
    return template.render(context)


def send_email(recipient, subject, html_body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_TOKEN)
        server.send_message(msg)


def process_string_length():
    data = input_group(
        "Розрахунок довжини рядка",
        [
            input("Ваше ім'я", name="username", type=TEXT, required=True),
            input("Введіть рядок", name="user_string", type=TEXT, required=True),
            input(
                "Ваш Email для результату",
                name="email",
                type=TEXT,
                required=True,
            ),
        ],
    )

    cleaned_string = data["user_string"].strip()
    string_length = len(cleaned_string)

    context = {
        "name": data["username"],
        "original_string": cleaned_string,
        "length": string_length,
    }

    try:
        html_content = render_email_body("string.html", context)

        send_email(
            recipient=data["email"],
            subject="Результат обчислення довжини рядка",
            html_body=html_content,
        )

        put_success(f"Лист надіслано на адресу {data['email']}.")
        put_text(
            f"Привіт, {data['username']}. Обчислена довжина: {string_length} симв."
        )
    except Exception as e:
        put_error(f"Виникла помилка при відправці листа: {e}")

if __name__ == "__main__":
    start_server(process_string_length, port=8080)
