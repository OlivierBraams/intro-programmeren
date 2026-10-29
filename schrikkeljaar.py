def schrikkeljaar(jaar: int) -> bool:
    """
    >>> schrikkeljaar(200)
    False
    >>> schrikkeljaar(10)
    False
    >>> schrikkeljaar(800)
    True
    >>> schrikkeljaar(4000)
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
    

if __name__ == '__main__':
    jaar = int(input("Geef een jaartal: "))
    if is_acidic(ph):
        print(f"{jaar} is een schrikkeljaar")
    else:
        print(f"{jaar} is geen schrikkeljaar")