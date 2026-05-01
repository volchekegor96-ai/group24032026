from messages import *

name_input = input(MSG_INPUT_NAME).strip()
if name_input.isalpha():
    print(MSG_NAME_OK.format(name=name_input.title()))
else:
    print("Ім'я має містити лише літери.")

age_input = input(MSG_INPUT_AGE).strip().lstrip('0')
if age_input.isdigit():
    print(MSG_AGE_OK.format(age=age_input))
else:
    print("Вік має бути цілим числом.")

phone_input = input(MSG_INPUT_PHONE).replace(" ", "")
if phone_input.isdigit():
    print(MSG_PHONE_OK.format(phone=phone_input))
else:
    print("Номер телефону має містити лише цифри.")

print(MSG_FINISH)