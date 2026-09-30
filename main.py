import random
class Peli:
    def __init__(self):
        self.nopat = [0, 0, 0, 0, 0]
        self.kategoriat = {
            "Ykkoset": None,
            "Kakkoset": None,
            "Kolmoset": None,
            "Neloset": None,
            "Viitoset": None,
            "Kuutoset": None
        }

    def heita_nopat(self, pidetyt):
        for i in range(5):
            if i not in pidetyt:
                self.nopat[i] = random.randint(1, 6)

    def nayta_nopat(self):
        print("Nopat:", self.nopat)

    def vuoro(self):
        pidetyt = []

        for kierros in range(3):
            print(f"\nKierros {kierros + 1}")
            self.heita_nopat(pidetyt)
            self.nayta_nopat()

            if kierros < 2:
                syote = input("Mitkä nopat haluat pitää? ")
                
                if syote:
                    pidetyt = [int(x) - 1 for x in syote.split()]
                else:
                    pidetyt = []

    def laske_pisteet(self, kategoria):

        if kategoria == "Ykkoset":
            return self.nopat.count(1)

        elif kategoria == "Kakkoset":
            return self.nopat.count(2) * 2

        elif kategoria == "Kolmoset":
            return self.nopat.count(3) * 3

        elif kategoria == "Neloset":
            return self.nopat.count(4) * 4

        elif kategoria == "Viitoset":
            return self.nopat.count(5) * 5

        elif kategoria == "Kuutoset":
            return self.nopat.count(6) * 6

        for kategoria, pisteet in self.kategoriat.items():
            if pisteet is None:
                print(f"{kategoria}: -")
            else:
                print(f"{kategoria}: {pisteet}")
                
    def valitse_kategoria(self):
        vapaat = []

        for kategoria in self.kategoriat:
            if self.kategoriat[kategoria] is None:
                vapaat.append(kategoria)

        print("\nValitse kategoria:")

        for i, kategoria in enumerate(vapaat, 1):
            print(f"{i}. {kategoria}")

        while True:
            try:
                valinta = int(input("Valinta: "))

                if 1 <= valinta <= len(vapaat):
                    return vapaat[valinta - 1]
                
                print("Virheellinen valinta.")
            except ValueError:
                print("Anna numero.")

    def pelaa(self):

        while None in self.kategoriat.values():
            print("\n====================")
            print("UUSI VUORO")
            print("====================")

            self.vuoro()
            kategoria = self.valitse_kategoria()
            pisteet = self.laske_pisteet(kategoria)
            self.kategoriat[kategoria] = pisteet
            print(f"\nSait {pisteet} pistettä kategoriasta {kategoria}")

if __name__ == "__main__":
    peli = Peli()
    peli.pelaa()