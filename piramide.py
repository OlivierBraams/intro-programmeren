def piramide(hoogte: int) -> None:
    for i in range(2, hoogte + 1):
        for j in range(i):
            print('#', end = '') 




if __name__ == '__main__':
    hoogte = 0
    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
        
    piramide(hoogte)
    