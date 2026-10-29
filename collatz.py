def collatz_length(n):
    teller = 0
    while n != 1:
        if n % 2 == 0: 
            n / 2
        else:
            n * 3 + 1
        
        teller += 1
        
    return teller
    
int(input)

