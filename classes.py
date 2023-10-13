"""
Classes and Objects Exercises
https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes
"""

# Exercise 1
# Create a Class with instance attributes
class Vehicle:
    
    # Exercise 5
    # Define a property that must have the same value for every class instance (object)
    color = 'white'
    
    def __init__(self, name: str, max_speed: int, mileage: int, capacity: int) -> None:
        self.__name = name
        self.__max_speed = max_speed
        self.__mileage = mileage
        self.__capacity = capacity
        
    def display_info(self) -> None:
        print(f'Color: {self.color}')
        print(f'Name: {self.__name}')
        print(f'Max Speed: {self.__max_speed}')
        print(f'Mileage: {self.__mileage}')
        
    def seating_capacity(self) -> str:
        return f"The seating capacity of a {self.__name} is {self.__capacity} passengers"
    
    def fare(self) -> int:
        return self.__capacity * 100
        
        
# Exercise 2
# Create a Vehicle class without any variables and methods
"""
class Vehicle:
    pass
"""


# Exercise 3
# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self, name: str, max_speed: int, mileage: int, capacity: int) -> None:
        super().__init__(name, max_speed, mileage, capacity)
        
    # Exercise 4
    # Class Inheritance
    def seating_capacity(self) -> None:
        return super().seating_capacity()
    
    # Exercise 6
    # Class Inheritance
    def fare(self) -> int:
        amount = super().fare() 
        amount += amount * 10 / 100
        
        return amount


class Car(Vehicle):
    pass


def main() -> None:
    schoolbus = Bus('School Bus', 180, 12, 50)
    schoolbus.display_info()
    print(schoolbus.seating_capacity())
    print(schoolbus.fare())
    # Exercise 7
    # Check type of an object
    print(type(schoolbus))
    # Exercise 8
    # Determine if School_bus is also an instance of the Vehicle class
    print(isinstance(schoolbus, Vehicle))
    
    print('')
    car = Car('Volvo', 200, 15, 4)
    car.display_info()
    print(car.seating_capacity())

if __name__ == '__main__':
    main()
    