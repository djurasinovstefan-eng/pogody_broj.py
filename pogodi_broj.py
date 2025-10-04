# Pogodi broj - jednostavna igra
import random


def pogodi_broj():
    broj_za_pogadjanje = random.randint(1, 100)
    print("Pogodi broj od 1 do 100!")
    while True:
        try:
            pokusaj = int(input("Unesi svoj broj: "))
        except ValueError:
            print("Molim te, unesi ceo broj.")
            continue
        if pokusaj < broj_za_pogadjanje:
            print("Tvoj broj je manji od traženog.")
        elif pokusaj > broj_za_pogadjanje:
            print("Tvoj broj je veći od traženog.")
        else:
            print(f"Bravo! Pogodio si broj {broj_za_pogadjanje}!")
            break


if __name__ == "__main__":
    pogodi_broj()
random.randint(1, 100)
