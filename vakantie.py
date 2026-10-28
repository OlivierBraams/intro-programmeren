def travel_costs(km: int) -> float:
    """
    >>> travel_costs(10)
    3
    >>> travel_costs(1000)
    260
    """
    return int(km * 0.13 * 2)

def overnight_costs(nights: int) -> float:
    """
    overnight_costs(2)
    120
    
    """
    return nights * 60

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    """
    return km + nights

if __name__ == '__main__':
    afstand = int(input("Hoe ver ga je weg in km? "))
    nachten = int(input("Hoeveel nachten is je verblijf? "))
    
    print(f"Jouw vakantie kost: {total_costs(travel_costs(afstand), overnight_costs(nachten))}")
    
