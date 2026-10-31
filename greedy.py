def count_coins(x: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    """
    restant = 100 * x
    
    kwartjes = 0
    dubbeltjes = 0
    stuivers = 0 
    centen = 0
    
    While x / 25 > 1:
        kwartjes = x - 25
    
    restant = restant  % 25
    
    While restant / 10 > 1: 
        dubbeltjes = restant - 10
    
    restant = restant % 10
    
    While restant / 5 > 1:
        stuivers = restant - 5
    
    restant = restant % 5
    
    While restant / 1 > 1:
        centen = restant - 1

if __name__ == '__main__':
    bedrag = 0
    while bedrag <= 0: 
        bedrag = float(input('Geef een correct bedrag: '))
        
        

