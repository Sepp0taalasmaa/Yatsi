from game.player import Player

class UI:
    def __init__(self):
        self.peli_kaynnissa = True

    def run(self, game):
        while game.peli_kaynnissa():
            print()
            print("=" * 40)
            print("                 YATZY")
            print("=" * 40)
            print("Pelaaja:", Player.nimi)


    