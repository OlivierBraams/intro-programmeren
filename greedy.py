def count_coins(x: float) -> int:
    """
    >>> count_coins(0.25)
    1
    >>> count_coins(1.01)
    5
    >>> count_coins(0.56)
    4
    """
    restant  = int(100 * x)
    
    kwartjes = 0
    dubbeltjes = 0
    stuivers = 0 
    centen = 0
    
    while restant >= 25:
        restant = restant - 25
        kwartjes += 1
    
    
    while restant >= 10: 
        restant = restant - 10
        dubbeltjes += 1
    
    
    
    while restant >= 5:
        restant = restant - 5
        stuivers += 1
    
    
    while restant >= 1:
        restant = restant - 1
        centen += 1
        
    return kwartjes + dubbeltjes + stuivers + centen

if __name__ == '__main__':
    bedrag = -1.0
    while bedrag < 0: 
        bedrag = float(input('Geef een correct bedrag: '))
    
    
    print(f"minimaal aantal munten: {count_coins(bedrag)}")
        
        

