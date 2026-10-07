from game.player import Player

class UI:

    def __init__(self, pelaaja: Player):
        self._pelaaja = pelaaja.nimi

    @property
    def peli(self):
        print(self._pelaaja)



