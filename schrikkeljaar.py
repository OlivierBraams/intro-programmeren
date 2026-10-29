def schrikkeljaar(jaar: int) -> bool:
    """
    >>> schrikkeljaar(200)
    False
    >>> schrikkeljaar(10)
    False
    >>> schrikkeljaar(800)
    True
    >>> schrikkeljaar(200)
    """
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0: 
                return True
            else:
                return False
    else:
        return True
    

if __name__ == '__main__':
    ph = int(input("Geef een pH-waarde: "))
    if is_acidic(ph):
        print("Het is een zuur")
    else:
        print("Het is een base")