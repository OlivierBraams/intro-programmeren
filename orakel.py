def check_answer(antwoord: str) -> bool:
    """
    >>> check_answer("42")
    True
    >>> check_answer("3")
    False
    >>> check_answer("tweeenveertig")
    True
    """
    if antwoord == "42" or antwoord == "tweeenveertig" or antwoord == "tweeënveertig":
        return True
    else:
        return False

if __name__ == '__main__':
    vraag = "Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij? "
    antwoord = input(vraag)
    if check_answer(antwoord):
        print("Ja")
    else: 
        print("Nee")
    