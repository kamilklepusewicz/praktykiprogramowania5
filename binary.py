"""kalkulator binarny"""


def licz(a):
    """kalkulator"""
    if isinstance(a, float):
        return "Podana wartosc nie jest liczba naturalna"
    if a > 100:
        return "Podana wartosc jest poza zakresem"
    wynik = bin(a)
    return str(wynik)
