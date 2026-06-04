"""task1"""
def calculate(a: int | float, b: int | float, operation: str = "sum") -> int | float:
    if operation == "sub":
        return a - b
    return a + b

"""task2"""
def format_string(text: str, upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()

"""task3"""
def sum_string_numbers(numbers_str: str, separator: str = ",") -> int | float:
    if not numbers_str.strip():
        return 0

    parts = numbers_str.split(separator)
    return sum(float(num.strip()) for num in parts)
