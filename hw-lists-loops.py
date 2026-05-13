numbers = [1, 5, 2, 8, 3, 7]
grades = [10, 8, 12, 7, 9]

max_num = max(numbers)
min_num = min(numbers)
total_sum = sum(numbers)

average_grade = sum(grades) / len(grades)
high_grades = [grade for grade in grades if grade > average_grade]

output_text = f"""Завдання 1
Список чисел: {numbers}
Найбільше число: {max_num}
Найменше число: {min_num}
Сума всіх чисел: {total_sum}

Завдання 2
Список оцінок учня: {grades}
Середній бал: {average_grade:.2f}
Оцінки вище середнього: {high_grades}"""

print(output_text)