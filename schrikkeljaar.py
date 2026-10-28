def schrikkeljaar(jaar: int) -> bool:
    """
    >>> is_acidic(2)
    True
    >>> is_acidic(9)
    False
    >>> is_acidic(7)
    False
    """
    if jaar % 100 == 0:
        if jaar % 400 == 0: 
            return True
        else:
            return False
   
    

if __name__ == '__main__':
    ph = int(input("Geef een pH-waarde: "))
    if is_acidic(ph):
        print("Het is een zuur")
    else:
        print("Het is een base")