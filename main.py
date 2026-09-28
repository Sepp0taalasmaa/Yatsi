import random
class Peli:


    def __init__(self):
        self.nopat = [0,0,0,0,0]

    def heita_nopat(self, pidetyt):
        for i in range(5):
            if i not in pidetyt:
                self.nopat[i] = random.randint(1,6)

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
                pidetyt = [int(x) - 1 for x in syote.split()]
    def pisteet(self):
        pass


if __name__ == "__main__":
    peli = Peli()
    peli.vuoro()

    
    