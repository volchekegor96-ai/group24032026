from pywebio import start_server
from pywebio.input import input, select, slider, NUMBER
from pywebio.output import put_text, put_markdown


def calculate_trip():
    put_markdown("Організатор шкільних поїздок")

    students = input("Введіть кількість учнів:", type=NUMBER)

    if students <= 0:
        put_text("Кількість учнів не може бути 0")
        return

    teachers = input("Введіть кількість вчителів:", type=NUMBER)
    transport_type = select("Оберіть транспорт:", ["Автобус", "Поїзд"])
    days = slider("Оберіть кількість днів поїздки:", min_value=0, max_value=14, step=1)

    total_people = students + teachers

    if days == 0:
        nights = 0
    else:
        nights = days - 1

    transport_cost = 0
    buses_needed = 0

    if transport_type == "Автобус":
        buses_needed = total_people // 40
        if total_people % 40 > 0:
            buses_needed = buses_needed + 1

        transport_cost = buses_needed * 5000

    if transport_type == "Поїзд":
        transport_cost = total_people * 300

    accommodation_cost = total_people * 400 * nights

    total_cost = transport_cost + accommodation_cost

    if total_people > 30:
        discount = total_cost * 0.10
        total_cost = total_cost - discount

    put_markdown("Результати розрахунку:")
    put_text("Загальна кількість людей:", total_people)

    if transport_type == "Автобус":
        put_text("Потрібно автобусів:", buses_needed)

    put_text("Вартість транспорту:", transport_cost, "грн.")
    put_text("Вартість проживання:", accommodation_cost, "грн.")
    put_text("Загальна сума:", total_cost, "грн.")


start_server(calculate_trip(), port=8080)