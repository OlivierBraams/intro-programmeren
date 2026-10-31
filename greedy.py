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
    
    While x // 25 > 0:
        kwartjes = x - 25
    
    restant = restant  % 25
    
    While restant // 10 > 0: 
        dubbeltjes = restant - 10 

if __name__ == '__main__':
    bedrag = -1
    while bedrag <= 0: 
        bedrag = float(input('Geef een correct bedrag: '))
        
        

