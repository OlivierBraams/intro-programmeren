def piramide(x: int) -> int:
    for i in range(2, x + 1):
        print('#', end = i)




if __name__ == '__main__':
    hoogte = 0
    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
        
    piramide(hoogte)
    