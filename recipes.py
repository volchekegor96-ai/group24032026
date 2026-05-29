import requests

url = "https://dummyjson.com/recipes"
response = requests.get(url)
data = response.json()
recipes = data.get("recipes", [])

pizza_recipes = []
italian_count = 0
max_calories_recipe = None
recipes_190 = []
total_reviews = 0

for r in recipes:
    name = r.get("name", "")
    if "pizza" in name.lower():
        pizza_recipes.append(name)

    if r.get("cuisine", "").lower() == "italian":
        italian_count += 1

    calories = r.get("caloriesPerServing", 0)
    if max_calories_recipe is None or calories > max_calories_recipe.get("caloriesPerServing", 0):
        max_calories_recipe = r

    instructions = r.get("instructions", [])
    for step in instructions:
        if "190" in step:
            recipes_190.append(name)
            break

    total_reviews += r.get("reviewCount", 0)

max_calories_name = max_calories_recipe.get("name", "Нет данных") if max_calories_recipe else "Нет данных"
max_calories_val = max_calories_recipe.get("caloriesPerServing", 0) if max_calories_recipe else 0

print(
    f"Рецепти піци: {', '.join(pizza_recipes)}\n"
    f"Кількість італійських страв: {italian_count}\n"
    f"Найкалорійніша страва: {max_calories_name} ({max_calories_val} kcal)\n"
    f"Готуються при 190°C: {', '.join(recipes_190)}\n"
    f"Загальна кількість переглядів: {total_reviews}"
)
