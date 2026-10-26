if __name__ == '__main__':
    
    day1 = int(input("Dagnummer 1: "))
    day2 = int(input("Dagnummer 2: "))
    print(f"Er zijn {result} volle weken verstreken.")


def weeks_elapsed(x,y):
    """
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    """
    result = abs(day2 - day1) // 7
    return result

