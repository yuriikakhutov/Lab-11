from datetime import datetime

class Car:
    _id_counter = 0  # Класова змінна для генерації унікального id

    def __init__(self, brand, model, year_of_manufacture, color, price, registration_number):
        Car._id_counter += 1
        self.id = Car._id_counter
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.color = color
        self.price = price
        self.registration_number = registration_number

    def __str__(self):
        return (f"Car(id={self.id}, brand={self.brand}, model={self.model}, "
                f"year_of_manufacture={self.year_of_manufacture}, color={self.color}, "
                f"price={self.price}, registration_number={self.registration_number})")

    # Геттери та сеттери з валідацією
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        if not value:
            raise ValueError("Brand cannot be empty")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        if not value:
            raise ValueError("Model cannot be empty")
        self._model = value

    @property
    def year_of_manufacture(self):
        return self._year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, value):
        if not isinstance(value, int):
            raise ValueError("Year of manufacture must be an integer")
        current_year = datetime.now().year
        if value < 1886 or value > current_year:  # 1886 is regarded as the year of the first car
            raise ValueError(f"Year of manufacture must be between 1886 and {current_year}")
        self._year_of_manufacture = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise ValueError("Color must be a string")
        if not value:
            raise ValueError("Color cannot be empty")
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, value):
        if not isinstance(value, str):
            raise ValueError("Registration number must be a string")
        if not value:
            raise ValueError("Registration number cannot be empty")
        self._registration_number = value


class CarFleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def cars_by_brand(self, brand):
        return [car for car in self.cars if car.brand == brand]

    def cars_by_model_and_age(self, model, years):
        current_year = datetime.now().year
        return [car for car in self.cars if car.model == model and (current_year - car.year_of_manufacture) > years]

    def cars_by_year_and_price(self, year, min_price):
        return [car for car in self.cars if car.year_of_manufacture == year and car.price > min_price]


# Демонстрація використання
fleet = CarFleet()
fleet.add_car(Car("Toyota", "Corolla", 2019, "White", 20000, "AA0011BB"))
fleet.add_car(Car("Ford", "Fiesta", 2018, "Blue", 15000, "AA0022BB"))
fleet.add_car(Car("Toyota", "Camry", 2020, "Black", 25000, "AA0033BB"))

print("Cars by brand 'Toyota':")
for car in fleet.cars_by_brand("Toyota"):
    print(car)

print("\nCars by model 'Corolla' used more than 3 years:")
for car in fleet.cars_by_model_and_age("Corolla", 3):
    print(car)

print("\nCars from year 2018 with price higher than 16000:")
for car in fleet.cars_by_year_and_price(2018, 16000):
    print(car)
