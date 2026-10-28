def weeks_elapsed(x,y):
    """
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    result = abs(x - y) // 7
    return result




if __name__ == '__main__':
    
    day1 = int(input("Dagnummer 1: "))
    day2 = int(input("Dagnummer 2: "))
    
    weeks_elapsed(day1, day2)
    print(f"Er zijn {weeks_elapsed(day1, day2)")
    


