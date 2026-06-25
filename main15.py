from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, fuel: float, condition: float):
        self.fuel = int(fuel)
        self._condition = max(0, min(100, int(condition)))

    @property
    def condition(self) -> int:
        return self._condition

    @condition.setter
    def condition(self, value: float):
        self._condition = max(0, min(100, int(value)))

    @property
    def is_working(self) -> bool:
        return self.condition > 20

    @abstractmethod
    def __str__(self) -> str:
        pass

    def move(self, distance: float):
        if not self.is_working:
            print(f"{self.__class__.__name__} зламався, рух неможливий")
            return

        fuel_needed = distance * 0.1
        if self.fuel < fuel_needed:
            print(f"Недостатньо пального для подорожі на {int(distance)} км")
            return

        self.fuel = int(self.fuel - fuel_needed)
        self.condition = int(self.condition - distance * 0.2)
        print(f"{self.__class__.__name__} проїхав {int(distance)} км")


class Car(Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100)
        self.model = model

    def __str__(self) -> str:
        return f"Автомобіль {self.model}  Пальне: {self.fuel}  Стан: {self.condition}%  Працює: {self.is_working}"


class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100)
        self.name = name

    def __str__(self) -> str:
        return f"Вантажівка {self.name}  Пальне: {self.fuel}  Стан: {self.condition}%  Працює: {self.is_working}"


class Motorcycle(Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20, condition=100)
        self.brand = brand

    def __str__(self) -> str:
        return f"Мотоцилк {self.brand}  Пальне: {self.fuel}  Стан: {self.condition}%  Працює: {self.is_working}"


class ServiceStation:
    def repair(self, transport_unit: Transport):
        if transport_unit.condition == 100:
            print(f"Ремонт не треба, {transport_unit.__class__.__name__} в ідеальному стані.")
            return

        transport_unit.condition += 40
        print(f"Ремонт зроблено, стан {transport_unit.__class__.__name__}: {transport_unit.condition}%")


car = Car("Toyota Camry")
truck = Truck("Volvo FH16")
motorcycle = Motorcycle("Yamaha R1")

print(car)
print(truck)
print(motorcycle)

car.move(100)
print(car)
print(car.__dict__)

motorcycle.move(250)

truck.move(450)
print(truck)
print(truck.is_working)
truck.move(10)

station = ServiceStation()

station.repair(car)

station.repair(truck)
print(truck.is_working)

station.repair(truck)
print(truck)
