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

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    >>> is_same_square(3,3,3,3)
    True
    >>> is_same_square(1,2,3,4)
    False
    """
    if ax_length == ay_length and bx_length == by_length and ax_length == bx_:
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
    return abs(c2 - c1)
    

if __name__ == '__main__':
    ax1 = int(input("Geef de x1 van A: "))
    ax2 = int(input("Geef de x2 van A: "))
    ay1 = int(input("Geef de y1 van A: "))
    ay2 = int(input("Geef de y2 van A: "))
    bx1 = int(input("Geef de x1 van B: "))
    bx2 = int(input("Geef de x2 van B: "))
    by1 = int(input("Geef de y1 van B: "))
    by2 = int(input("Geef de y2 van B: "))
    
    ax = calculate_length(ax1,ax2)
    ay = calculate_length(ay1,ay2)
    bx = calculate_length(bx1,bx2)
    by = calculate_length(by1,by2)
    
    if is_same_rectangle(ax, ay, bx, by):
        if is_same_square(ax,ay,bx,by):
            print("De rechthoeken zijn gelijk!")
            print("En ze zijn ook nog vierkant!")
        else:
            print("De rechthoeken zijn gelijk!")
    else:
        print("Er is niks aan :( ")
