def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    
    """
    
    a = coffee * 90
    b = tea * 45
    c = energy * 80
    d = cola * 40
    
    return a + b + c + d 


if __name__ == '__main__':
    koffie = int(input("hoeveel koppen koffie? "))
    thee = int(input("hoeveel koppen thee? "))
    energiedrank = int(input("hoeveel energiedrankjes? "))
    cola = int(input("hoeveel glazen cola? "))
    
    print (f"je krijgt {calculate_cafeine(koffie, thee, energiedrank, cola)} mg cafeïne binnen.")