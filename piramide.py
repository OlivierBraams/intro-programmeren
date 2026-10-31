def piramide(hoogte: int) -> None:
    """
    >>> piramide(5)
    ##
    ###
    ####
    #####
    >>> piramide(2)
    ##
    >>> piramide(4)
    ##
    ###
    ####
    """
    for i in range(1, hoogte + 1):
        for j in range(i ):
            print('#', end = '')
        print("#")




if __name__ == '__main__':
    hoogte = 0
    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
        
    piramide(hoogte)
    