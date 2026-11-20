from __future__ import annotations
from math import isfinite


def positive(value: float) -> None:
    if not isfinite(value) or value <= 0:
        raise ValueError('Значення повинно бути додатним скінченним числом.')


class Vehicle:
    """Базовий транспортний засіб із лічильником пробігу."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make, self.model, self.year = make, model, year
        self._mileage = 0.0

    @property
    def mileage(self) -> float:
        return self._mileage

    def drive(self, km: float) -> str:
        positive(km)
        self._mileage += km
        return f'{self.make} {self.model}: подолано {km:g} км.'

    def refuel(self, liters: float) -> str:
        positive(liters)
        return f'{self.make}: заправлено {liters:g} л.'

    def status(self) -> str:
        return f'{self.make} {self.model}, {self.year}; пробіг: {self.mileage:g} км'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.make!r}, {self.model!r}, {self.year})'


class Car(Vehicle):
    """Автомобіль із витратою палива 8 літрів на 100 кілометрів."""

    CONSUMPTION = 8.0

    def __init__(self, make: str, model: str, year: int,
                 fuel_type: str = 'бензин', fuel_level: float = 0.0) -> None:
        super().__init__(make, model, year)
        if not isfinite(fuel_level) or fuel_level < 0:
            raise ValueError('Рівень палива не може бути від’ємним.')
        self.fuel_type, self.fuel_level = fuel_type, float(fuel_level)

    @property
    def range(self) -> float:
        return self.fuel_level / self.CONSUMPTION * 100

    def drive(self, km: float) -> str:
        positive(km)
        needed = km * self.CONSUMPTION / 100
        if needed > self.fuel_level:
            raise ValueError(f'{self.make}: недостатньо палива.')
        message = super().drive(km)
        self.fuel_level -= needed
        return message + f' Витрачено {needed:g} л.'

    def refuel(self, liters: float) -> str:
        message = super().refuel(liters)
        self.fuel_level += liters
        return message

    def status(self) -> str:
        return (super().status() + f'; {self.fuel_type}: {self.fuel_level:g} л; '
                f'запас ходу: {self.range:g} км')


class ElectricCar(Car):
    """Електромобіль із запасом ходу 400 км за повного заряду."""

    FULL_RANGE = 400.0

    def __init__(self, make: str, model: str, year: int,
                 battery_level: float = 100.0) -> None:
        super().__init__(make, model, year, 'електрика', 0)
        if not 0 <= battery_level <= 100:
            raise ValueError('Заряд повинен бути від 0 до 100%.')
        self.battery_level = float(battery_level)

    @property
    def range(self) -> float:
        return self.FULL_RANGE * self.battery_level / 100

    def drive(self, km: float) -> str:
        positive(km)
        needed = km / self.FULL_RANGE * 100
        if needed > self.battery_level:
            raise ValueError(f'{self.make}: недостатньо заряду.')
        self._mileage += km
        self.battery_level -= needed
        return f'{self.make}: подолано {km:g} км, витрачено {needed:g}% заряду.'

    def refuel(self, liters: float) -> str:
        raise TypeError('Електромобіль потрібно заряджати методом charge().')

    def charge(self, percent: float) -> str:
        positive(percent)
        if self.battery_level + percent > 100:
            raise ValueError('Заряд після заряджання перевищить 100%.')
        self.battery_level += percent
        return f'{self.make}: заряджено до {self.battery_level:g}%.'

    def status(self) -> str:
        return (f'{self.make} {self.model}, {self.year}; пробіг: {self.mileage:g} км; '
                f'заряд: {self.battery_level:g}%; запас ходу: {self.range:g} км')


class Truck(Vehicle):
    """Вантажівка з контролем вантажопідйомності."""

    def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
        super().__init__(make, model, year)
        positive(capacity)
        self.capacity = capacity
        self.cargo_weight = 0.0

    def load(self, kg: float) -> None:
        positive(kg)
        if self.cargo_weight + kg > self.capacity:
            raise ValueError('Перевищено вантажопідйомність.')
        self.cargo_weight += kg

    def unload(self, kg: float) -> None:
        positive(kg)
        if kg > self.cargo_weight:
            raise ValueError('Не можна вивантажити більше, ніж завантажено.')
        self.cargo_weight -= kg

    def drive(self, km: float) -> str:
        return super().drive(km) + f' Перевезено {self.cargo_weight:g} кг вантажу.'

    def status(self) -> str:
        return super().status() + f'; вантаж: {self.cargo_weight:g}/{self.capacity:g} кг'


class FleetManager:
    """Керує транспортом і формує загальний звіт автопарку."""

    def __init__(self) -> None:
        self.vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        if not isinstance(vehicle, Vehicle):
            raise TypeError('Очікується транспортний засіб.')
        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles.remove(vehicle)

    def total_mileage(self) -> float:
        return sum(v.mileage for v in self.vehicles)

    def find_by_make(self, make: str) -> list[Vehicle]:
        return [v for v in self.vehicles if v.make.casefold() == make.casefold()]

    def report(self) -> str:
        return '\n'.join(v.status() for v in self.vehicles) + (
            f'\nТранспортних засобів: {len(self.vehicles)}'
            f'\nЗагальний пробіг: {self.total_mileage():g} км'
        )


def main() -> None:
    fleet = FleetManager()
    car1 = Car('Toyota', 'Corolla', 2020, 'бензин', 20)
    car2 = Car('Skoda', 'Octavia', 2021, 'дизель', 25)
    electric1 = ElectricCar('Tesla', 'Model 3', 2023, 80)
    electric2 = ElectricCar('Nissan', 'Leaf', 2022, 70)
    truck1 = Truck('Volvo', 'FH', 2019, 20000)
    truck2 = Truck('MAN', 'TGX', 2020, 18000)
    for vehicle in [car1, car2, electric1, electric2, truck1, truck2]:
        fleet.add_vehicle(vehicle)
    truck1.load(5000)
    truck2.load(3000)
    print(car1.refuel(5))
    print(electric1.charge(10))
    print('\n--- Поліморфізм: drive(100) ---')
    for vehicle in fleet.vehicles:
        print(vehicle.drive(100))
    truck1.unload(1000)
    print('\n--- Звіт ---\n' + fleet.report())
    print('\nПошук Toyota:', fleet.find_by_make('toyota'))
    fleet.remove_vehicle(truck2)
    print('Після видалення MAN:', len(fleet.vehicles))
    fleet.add_vehicle(truck2)
    for action in [lambda: truck1.load(30000), lambda: truck1.unload(9000),
                   lambda: car1.drive(10000), lambda: electric1.refuel(10)]:
        try:
            action()
        except (ValueError, TypeError) as error:
            print('Перевірка помилки:', error)


if __name__ == '__main__':
    main()
