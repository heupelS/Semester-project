class Feld:
    def __init__(self, wert, position):
        if wert == "Leer" or wert == "XXXX" or wert == "OOOO":
            self.wert = wert
            self.position = position;
        else:
            print("raff dich!")


def setup():
    return [Feld("Leer", 11), Feld("Leer", 12), Feld("Leer", 13), Feld("Leer", 21), Feld("Leer", 22), Feld("Leer", 23),
            Feld("Leer", 31), Feld("Leer", 32), Feld("Leer", 33)]


def main():
    spieler = 1
    spielersymbol = "XXXX"
    Spielfeld = setup();

    print_spielfeld(Spielfeld)
    while True:
        winner = winner_winner_chicken_dinner(Spielfeld)
        if (winner != 0):
            print("Spieler " + str(winner) + " hat gewonnen!")
            eingabe = input("you wanna regame? (Y/N)")
            if eingabe == "Y":
                main()
            else:
                return

        while True:
            inputt = int(input("\n\nSpieler " + str(spieler) + ": "))
            if gültigeEingabe(inputt, Spielfeld):
                break
            else:
                print_spielfeld(Spielfeld)

        for x in range(0, len(Spielfeld)):
            if Spielfeld[x].position == inputt and Spielfeld[x].wert == "Leer":
                Spielfeld[x] = Feld(spielersymbol, inputt)
                break

        print_spielfeld(Spielfeld)
        if spieler == 1:
            spieler = 2
        else:
            spieler = 1

        if spielersymbol == "XXXX":
            spielersymbol = "OOOO"
        else:
            spielersymbol = "XXXX"


def gültigeEingabe(spielzug, Spielfeld):
    if (spielzug >= 11 and spielzug <= 13) or (spielzug >= 21 and spielzug <= 23) or (
            spielzug >= 31 and spielzug <= 33):
        for x in range(0, len(Spielfeld)):
            if Spielfeld[x].wert == "Leer" and Spielfeld[x].position == spielzug:
                return True
    else:
        return False


def print_spielfeld(Spielfeld):
    print(Spielfeld[0].wert + "\t" + Spielfeld[1].wert + "\t" + Spielfeld[2].wert + "\n\n" + Spielfeld[3].wert + "\t" +
          Spielfeld[4].wert + "\t" + Spielfeld[5].wert + "\n\n" + Spielfeld[6].wert + "\t" + Spielfeld[7].wert + "\t" +
          Spielfeld[8].wert)


def winner_winner_chicken_dinner(x):
    if x[0].wert == x[3].wert == x[6].wert and x[0].wert != "Leer":
        if x[0] == "XXXX":
            return 1
        else:
            return 2
    elif x[1].wert == x[4].wert == x[7].wert and x[1].wert != "Leer":
        if x[1] == "XXXX":
            return 1
        else:
            return 2
    elif x[2].wert == x[5].wert == x[8].wert and x[2].wert != "Leer":
        if x[2] == "XXXX":
            return 1
        else:
            return 2
    elif x[0].wert == x[1].wert == x[2].wert and x[0].wert != "Leer":
        if x[0] == "XXXX":
            return 1
        else:
            return 2
    elif x[3].wert == x[4].wert == x[5].wert and x[3].wert != "Leer":
        if x[3] == "XXXX":
            return 1
        else:
            return 2
    elif x[6].wert == x[7].wert == x[8].wert and x[6].wert != "Leer":
        if x[6] == "XXXX":
            return 1
        else:
            return 2
    elif x[0].wert == x[4].wert == x[8].wert and x[0].wert != "Leer":
        if x[0] == "XXXX":
            return 1
        else:
            return 2
    elif x[2].wert == x[4].wert == x[6].wert and x[2].wert != "Leer":
        if x[0] == "XXXX":
            return 1
        else:
            return 2

    else:
        return 0


main()
