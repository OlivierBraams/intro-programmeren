def calculate_years(start_size: int, end_size: int) -> int:
    """
    >>> calculate_years(1200, 1300)
    1
    >>> calculate_years(9,18)
    8
    >>> calculate_years(20,100)
    20
    """
    jaar = 0
    while start_size < end_size:
        start_size = start_size + start_size / 3 - start_size / 4
        jaar += 1
        print(jaar)
       
    return jaar 

if __name__ == '__main__':
    startpopulatie = 1
    while startpopulatie < 9: 
        startpopulatie = int(input("startgrootte: "))
    
    eindpopulatie = 0
    while eindpopulatie <= startpopulatie:
        eindpopulatie = int(input("eindgrootte: "))
    
    print(f"Jaren: {calculate_years(startpopulatie, eindpopulatie)}")
