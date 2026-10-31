def piramide(hoogte: int) -> int:
    for i in range(2, hoogte + 1):
        for j in range(i):
            print('#') 




if __name__ == '__main__':
    hoogte = 0
    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
        
    piramide(hoogte)
    