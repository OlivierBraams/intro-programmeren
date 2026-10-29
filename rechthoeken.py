def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    >>> is_same_rectangle(3,2,3,2)
    True
    >>> is_same_rectangle(5,2,3,2)
    False
    """
    if ax_length == bx_length and ay_length == by_length:
        return True
    else: 
        return False

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> TODO:
    """
    >>> is_same_square(3,3,3,3)
    True
    >>> is_same_square(1,2,3,4)
    False
    """
    if ax_length == ay_length and bx_length == by_length:
        return True
    else: 
        return False

def calculate_length(c1: int, c2: int) -> int:
    """
    >>> calculate_length(3,5)
    2
    >>> calculate_length(8,12)
    4
    >>> calculate_length(1,5)
    4
    """
    return c2 - c1
    

if __name__ == '__main__':
    ax1 = int(input("Geef de x1 van A: "))
    ax2 = int(input("Geef de x2 van A: "))
    ay1 = int(input("Geef de y1 van A: "))
    ay2 = int(input("Geef de y2 van A: "))
    bx1 = int(input("Geef de x1 van B: "))
    bx2 = int(input("Geef de x2 van B: "))
    by1 = int(input("Geef de y1 van B: "))
    by2 = int(input("Geef de y2 van B: "))
    
    if is_same_rectangle(calculate_length(ax1, ax2), calculate_length(ay1,ay2), calculate_length(bx1,bx2), calculate_length(by1,by2)):
        if is_same_square(calculate_length(ax1, ax2), calculate_length(ay1,ay2), calculate_length(bx1,bx2), calculate_length(by1,by2)):
            print("De rechthoeken zijn gelijk!")
            print("En ze zijn ook nog vierkant!")
        else:
            print("De rechthoeken zijn gelijk!")
    else:
        print("De rechthoeken zijn niet gelijk")
