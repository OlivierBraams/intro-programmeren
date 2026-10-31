def count_coins(x: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    """
    bedrag = 100 * x
    
    kwartjes = 0
    dubbeltjes = 0
    stuivers = 0 
    centen = 0
    
    While bedrag > 25:
        restant = bedrag - 25
        kwartjes += 1
    
    
    While restant > 10: 
        restant = restant - 10
        dubbeltjes += 1
    
    
    
    While restant > 5:
        restant = restant - 5
        stuivers += 1
    
    
    While restant > 1:
        restant = restant - 1
        centen += 1
        
    return kwartjes, dubbeltjes, stuivers, centen

if __name__ == '__main__':
    bedrag = 0
    while bedrag <= 0: 
        bedrag = float(input('Geef een correct bedrag: '))
    
    kwartjes, dubbeltjes, stuivers, centen = count_coins(bedrag)
    print(f"kwartjes: {kwartjes}, dubbeltjes: {dubbeltjes}")
        
        

