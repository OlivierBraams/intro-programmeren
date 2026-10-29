def is_schrikkel(jaar: int) -> bool:
    """
    >>> is_schrikkel(200)
    False
    >>> is_schrikkel(10)
    False
    >>> is_schrikkel(800)
    True
    >>> is_schrikkel(4000)
    True
    """
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0: 
                return True
            else: 
                return False
        else:
            return True
    else:
        return False
    

if __name__ == '__main__':
    jaar = int(input("Geef een jaartal: "))
    if is_schrikkel(jaar):
        print(f"{jaar} is een schrikkeljaar")
    else:
        print(f"{jaar} is geen schrikkeljaar")