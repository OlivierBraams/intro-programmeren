def get_positive_int():
    getal = 0
    while getal % 2 != 0 or getal < 1:
        getal = int(input("Geef een positief even getal: "))

def get_any_int_but_0():
    getal = 0
    while getal == 0:
        getal = int(input("Geef een ander getal dan 0: "))

def get_min_int(minimum):
    
    while getal == 0:
        getal = int(input("Geef een ander getal dan 0: "))
        
        
        
if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    # get_min_int(100)
    # get_two_different_ints()