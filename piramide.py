def piramide(x: int) -> int:
    for i in (x + 1):
        print('#', end = '')




if __name__ == '__main__':
    hoogte = -3
    while hoogte < 1 and grootte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
        
    piramide(hoogte)
    