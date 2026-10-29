def collatz_length(n):
    while n != 1:
        if n % 2 == 0: 
            n / 2
        else:
            n * 3 + 1
        
        