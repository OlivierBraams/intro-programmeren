def calculate_years(start_size: int, end_size: int) -> int:
    """
    >>> calculate_years()
    """
    jaar = 0
    while start_size < end_size:
        start_size += start_size / 3
        start_size -= start_size / 4
        jaar += 1
       
    return jaar 

if __name__ == '__main__':
    startpopulatie = 1
    while startpopulatie <= 9: 
        startpopulatie = int(input("startgrootte: "))
    
    eindpopulatie = 0
    while eindpopulatie <= startpopulatie:
        eindpopulatie = int(input("eindgrootte: "))
