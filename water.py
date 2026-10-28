def hoeveelheid_water(minuten: int) -> int:
    """
    >>> hoeveelheid_water(10)
    120
    >>> hoeveelheid_water(3)
    36
    >>> hoeveelheid_water(6)
    72
    """
    water = minuten * 12
    return water
    
    
    

if __name__ == '__main__':
    minuten = int(input("Hoeveel minuten douche je? " ))
    print(hoeveelheid_water(minuten))
    