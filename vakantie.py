def travel_costs(km: int) -> float:
    """
    >>> travel_costs(10)
    2.6
    >>> travel_costs(1000)
    260
    """
    return km * 0.13 * 2

def overnight_costs(nights: int) -> float:
    """
    >>> overnight_costs(2)
    120
    >>> overnight_costs(10)
    600
    """
    return nights * 60

def total_costs(km: int, nights: int) -> int:
    """
    total_costs(10)
    """
    return int(km + nights)

if __name__ == '__main__':
    afstand = int(input("Hoe ver ga je weg in km? "))
    nachten = int(input("Hoeveel nachten is je verblijf? "))
    
    print(f"Jouw vakantie kost: {total_costs(travel_costs(afstand), overnight_costs(nachten))}")
    
