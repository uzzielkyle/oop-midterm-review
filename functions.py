# snake_case naming convention for function names and variables
def get_rect_perimeter(length: float, width: float) -> float:
    perimeter = round(2 * (length + width), ndigits=2)
    
    return perimeter


def main() -> None:
    square = {
        'length': 2,
        'width': 2,
    }
    
    rect = {
        'length': 4,
        'width': 2,
    }
    
    square_perimeter = get_rect_perimeter(square['length'], square['width'])
    print(f'Square\'s perimeter is {square_perimeter} units.')
    
    rect_perimeter = get_rect_perimeter(rect['length'], rect['width'])
    print(f'Rectangle\'s perimeter is {rect_perimeter} units.')
    
    
if __name__ == '__main__':
    main()
    