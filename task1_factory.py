"""
Завдання 1: Патерн фабрика для створення транспортних засобів
"""
from abc import ABC, abstractmethod

from logger import setup_logger

logger = setup_logger(__name__)


class Vehicle(ABC):
    """Абстрактний базовий клас для транспортних засобів"""

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """Абстрактний метод для запуску двигуна"""
        pass


class Car(Vehicle):
    """Клас автомобіля"""

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    """Клас мотоцикла"""

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    """Абстрактна фабрика для створення транспортних засобів"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів US специфікації"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів EU специфікації"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (EU Spec)")


def main() -> None:
    """Демонстрація роботи фабрик"""
    # US фабрика
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # EU фабрика
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("BMW", "X5")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")

    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
