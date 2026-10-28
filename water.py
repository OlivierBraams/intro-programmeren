def hoeveelheid_water(minuten: int) -> int:
    """
    >>>
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    """
    water = minuten * 12
    return water
    
    
    

if __name__ == '__main__':
    minuten = int(input("Hoeveel minuten douche je? " ))
    print(hoeveelheid_water(minuten))
    