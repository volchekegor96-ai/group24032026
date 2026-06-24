from pywebio import start_server
from pywebio.input import input, input_group, TEXT
from pywebio.output import put_text, put_success, put_error
import utils13


def check_email(val):
    if '@' not in val or '.' not in val:
        return 'Некоректний формат email'


def process_and_send(data: dict):
    username = data['username'].strip()
    user_string = data['user_string'].strip()
    email = data['email'].strip()

    string_length = len(user_string)

    context = {
        'username': username,
        'original_string': user_string,
        'string_length': string_length
    }

    try:
        html_body = utils13.generate_html_body('string.html', context)

        utils13.send_email(
            recipients=[email, 'volchekegor@ukr.net'],
            mail_body=html_body,
            mail_subject="Результат обчислення довжини стрічки"
        )

        put_success(f"Лист успішно надіслано на {email} та volchekegor@ukr.net!")
        put_text(f"Для користувача {username} обчислено довжину стрічки: {string_length}")
    except Exception as e:
        put_error(f"Виникла помилка при відправці: {e}")


def main():
    put_text("Обчислення довжини стрічки та відправки результатів на Укр.Нет ")

    form_data = input_group("Введіть дані", [
        input("Ваше ім'я", name='username', required=True),
        input("Введіть стрічку", name='user_string', required=True),
        input("Ваша пошта для результату", name='email', type=TEXT, validate=check_email, required=True)
    ])

    process_and_send(form_data)


if __name__ == '__main__':
    start_server(main, port=8080)
