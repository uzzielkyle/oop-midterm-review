# snake_case naming convention for function names and variables
def get_rect_perimeter(length: float, width: float) -> float:
    perimeter = round(2 * (length + width), ndigits=2)
    
    return perimeter


"""
Python Functions Exercise:
https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
"""

# Exercise 1
# Create a function in Python
def user_info(name: str, age: int) -> None:
    """Write a program to create a function that takes two arguments, name and age, and print their value.
    """
    print(f'Name: {name}')
    print(f'Age: {age}')
    

# Exercise 2
# Create a function with variable length of arguments
def func_1(*args) -> None:
    """Write a program to create function func1() to accept a variable length of arguments and print their value.
    """
    print('Printing values')
    [print(i) for i in args]

# Exercise 3
# Return multiple values from a function
def calculation(num_1: int, num_2: int) -> tuple[int]:
    """Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
    """
    sum = add_num(num_1, num_2)
    diff = sub_num(num_1, num_2)
    
    return sum, diff
    
# Modularity: Functions allow you to break down complex tasks into smaller, manageable parts, improving code organization and readability.
def add_num(x: int, y: int) -> int:
    sum = x + y
    return sum


def sub_num(x: int, y: int) -> int:
    diff = x - y
    return diff


# Exercise 4
# Create a function with a default argument
def show_employee(name: str, salary: int = 9000) -> None:
    """Write a program to create a function show_employee() using the following conditions.

    - It should accept the employee’s name and salary and display both.
    - If the salary is missing in the function call then assign default value 9000 to salary
    """ 
    print(f'Name: {name}, Salary: {salary}')
    
    
# Exercise 5
"""
Create an inner function to calculate the addition in the following way:
- Create an outer function that will accept two parameters, a and b
- Create an inner function inside an outer function that will calculate the addition of a and b
- At last, an outer function will add 5 into addition and return it
"""
def outer(a: int, b: int) -> int:
    
    def inner(a: int, b: int) -> int:
        sum = add_num(a, b)
        return sum
    
    final = add_num(inner(a, b), 5)
    return final


# Exercise 6
# Create a recursive function
def recursive_func(num: int = 10) -> int:
    """Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

    Args:
        num (int, optional): _description_. Defaults to 10.

    Returns:
        int: _description_
    """
    if not num:
        return num
    
    return num + recursive_func(num - 1)


# Exercise 7
# Assign a different name to function and call it through the new name
def display_student(name: str, age: int) -> None:
    print(name, age)
    
    
# Exercise 8
# Generate a Python list of all the even numbers between 4 to 30
def even_numbers(first_num: int = 4, last_num: int = 30) -> list[int]:
    evens = []
    
    for num in range(first_num, last_num, 2):
        evens.append(num)
        
    return evens


# Exercise 9
# Find the largest item from a given list
def largest_num(num_list: list[int]) -> int:
    largest = max(num_list)
    
    return largest


def main() -> None:
    my_name = 'Kyle'
    my_age = 21
    
    user_info(my_name, my_age)
    
    print('')
    func_1(2, 4, 6, 8, 9, 10, 23, 24, 26)
    
    print('')
    add, sub = calculation(24, 8)
    print(add, sub)
    
    print('')
    show_employee('Kyle', 250)
    show_employee('Nobody')
    
    print('')
    print(outer(23, 24))

    print('')
    print(recursive_func())
    
    print('')
    # Assign a different name to function and call it through the new name
    display_student(my_name, my_age)
    show_student = display_student
    show_student(my_name, my_age)
    
    print('')
    print(even_numbers())
    
    print('')
    x = [4, 6, 8, 24, 12, 2]
    print(largest_num(x))


if __name__ == '__main__':
    main()
    