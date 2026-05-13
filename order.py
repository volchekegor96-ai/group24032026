from letter import LETTER_TEMPLATE

client_name = input("Введіть своє ім'я та прізвище: ")
trip_date = input("Введіть дату поїздки (DD.MM.YYYY): ")
persons_count = int(input("Введіть кількість осіб: "))

PRICE_PER_PERSON = 15000

total_price = persons_count * PRICE_PER_PERSON

if persons_count > 5:
    discount = total_price * 0.05
else:
    discount = 0.0

final_price = total_price - discount

print(LETTER_TEMPLATE.format(
    name=client_name,
    date=trip_date,
    persons=persons_count,
    price_per_person=PRICE_PER_PERSON,
    total_price=total_price,
    discount=discount,
    final_price=final_price
))