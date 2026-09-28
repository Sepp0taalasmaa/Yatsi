import random
class Peli:
    def __init__(self):
        self.nopat = [0,0,0,0,0]

    def heitot(self):
        self.uudelleen = int(input("Montako uudelleen heittoa: "))
        
    def heita_nopat(self, pidetyt):
        for i in range(5):
            if i not in pidetyt:
                self.nopat[i] = random.randint(1,6)

    def nayta_nopat(self):
        print("Nopat:", self.nopat)

    def vuoro(self):
        pidetyt = []

        for kierros in range(self.uudelleen):
            print(f"\nKierros {kierros + 1}")

            self.heita_nopat(pidetyt)
            self.nayta_nopat()

            if kierros < self.uudelleen-1:
                syote = input("Mitkä nopat haluat pitää: ")
                pidetyt = [int(x) - 1 for x in syote.split()]

    def ykkoset(self):
        pisteet = 0
        for i in self.nopat:
            if i == 1:
                pisteet += 1
        print(pisteet)




if __name__ == "__main__":
    peli = Peli()
    peli.heitot()
    peli.vuoro()
    peli.ykkoset()


    

    
    