from functions import calculate, format_string, sum_string_numbers

print("Завдання 1")

res1_pos = calculate(10, 5, "sub")
print(f"Позиційні: {res1_pos}")

res1_kw = calculate(a=10, b=5, operation="sum")
print(f"Іменовані: {res1_kw}")

args1 = {"a": 20, "b": 7, "operation": "sub"}
res1_dict = calculate(**args1)
print(f"Розпакування dict: {res1_dict}")

print("\nЗавдання 2")

res2_pos = format_string("Hello World", False)
print(f"Позиційні: {res2_pos}")

res2_kw = format_string(text="Hello World", upper=True)
print(f"Іменовані: {res2_kw}")

args2 = {"text": "Python", "upper": False}
res2_dict = format_string(**args2)
print(f"Розпакування dict: {res2_dict}")

print("\nЗавдання 3")

res3_pos = sum_string_numbers("10;20;30", ";")
print(f"Позиційні: {res3_pos}")

res3_kw = sum_string_numbers(numbers_str="1,2,3", separator=",")
print(f"Іменовані: {res3_kw}")

args3 = {"numbers_str": "5 10 15", "separator": " "}
res3_dict = sum_string_numbers(**args3)
print(f"Розпакування dict: {res3_dict}")
