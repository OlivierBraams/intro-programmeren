def get_positive_int():
    getal = 0
    while getal % 2 != 0 or getal < 1:
        getal = int(input("Geef een positief even getal: "))

def get_any_int_but_0():
    getal = 0
    while getal == 0:
        getal = int(input("Geef een ander getal dan 0: "))

def get_min_int(minimum):
    getal = 0
    while  getal <= minimum:
        getal = int(input(f"Geef een groter getal dan {minimum}: "))
        
def get_min_int(minimum):
    getal1 = int(input("Geef een getal"))
    getal2 = getal1
    while  getal1 == getal2:
        getal2 == int(input("Geef nog een getal"))
        
        
if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    # get_two_different_ints()