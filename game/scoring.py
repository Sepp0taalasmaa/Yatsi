from scoring.scoring import calculate


class Scoring:
	def __init__(self):
		pass

	def calcScore(self, scard, dice: list[int], input: str):
		"""Legacy adapter: keep signature, but do not mutate scorecard."""
		return calculate(input, dice)