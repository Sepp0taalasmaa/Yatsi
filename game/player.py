from scorecard import Scorecard

class Player:
    def __init__(self, nimi):
        self._nimi = nimi
        self._scorecard = Scorecard()

    @property
    def nimi(self):
        return self._nimi

    @property
    def scorecard(self):
        return self._scorecard
    
    def total_score(self):
        return self._scorecard.scores