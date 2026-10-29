def collatz_length(n):
    teller = 0
    while n > 1:
        if n % 2 == 0: 
            n = n / 2
        else:
            n = n * 3 + 1
        
        teller += 1
        
    return teller

def print_collatz(n):
    print(n)
    while n > 1: 
        if n % 2 == 0:
            n = int(n / 2)
            print(n)
        else: 
            n = int(n * 3 + 1)
            print(n)



n = int(input("getal: "))
print_collatz(n)

