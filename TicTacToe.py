class Feld:
    def __init__(self, wert, position):
        if wert == "Leer" or wert == "Kreis" or wert == "Kreuz":
            self.wert = wert
            self.position = position;
        else:
            print("raff dich!")


def setup():
    Reihe1 = [Feld("Leer", 11), Feld("Leer", 12), Feld("Leer", 13)]
    Reihe2 = [Feld("Leer", 21), Feld("Leer", 22), Feld("Leer", 23)]
    Reihe3 = [Feld("Leer", 31), Feld("Leer", 32), Feld("Leer", 33)]
    Spielfeld = [Reihe1, Reihe2, Reihe3]


def main():
    win = False
    setup();
    while win == False:

