import datetime

class Car:
    def __init__(self, model: str, year: int, owner: str = "Немає власника", fuel: float = 0.0):
        self.model = model
        self.year = year
        self.owner = owner
        self.fuel = fuel

    def __str__(self) -> str:
        return f"Авто: {self.model} ({self.year} р.в.), Власник: {self.owner}, Пальне: {self.fuel} л"

    @property
    def condition(self) -> str:
        current_year = datetime.datetime.now().year
        age = current_year - self.year

        if age <= 3:
            return "нове авто"
        elif age <= 10:
            return "середній стан"
        else:
            return "старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 10:
            return "Потрібно заправитись"
        elif self.fuel <= 30:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"

car1 = Car(model="Toyota Camry", year=2024, fuel=5.0)  # Власник за замовчуванням
car2 = Car(model="BMW X5", year=2012, owner="Олександр", fuel=15.0)

print("Словники")
print(car1.__dict__)
print(car2.__dict__)
print()

print("Інформація про авто")
print(car1)
print(car2)
print()

print("Зміна кількості бензину")
car1.fuel = 55.0
car2.fuel = 8.0
print(f"в {car1.model} тепер є {car1.fuel} літрів бензину.")
print(f"в {car2.model} теперє {car2.fuel} літрів бензину.")
print()

print("Перевірка властивостей")
print(f"{car1.model}: стан {car1.condition}, статус пального {car1.fuel_status}")
print(f"{car2.model}: стан {car2.condition}, статус пального {car2.fuel_status}")
print()

print("Порівняння кількості бензину")
if car1.fuel > car2.fuel:
    print(f"В авто {car1.model} більше бензину ніж в {car2.model}.")
elif car1.fuel < car2.fuel:
    print(f"В авто {car2.model} більше бензину ніж в {car1.model}.")
else:
    print("В авто однакова кількість бензину.")
