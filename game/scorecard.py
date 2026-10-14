from collections import Counter

from scoring.scoring import calculate


CATEGORIES = (
	"Ykköset",
	"Kakkoset",
	"Kolmoset",
	"Neloset",
	"Viitoset",
	"Kuutoset",
	"Pari",
	"Kaksi paria",
	"Kolme samaa",
	"Neljä samaa",
	"Pieni suora",
	"Suuri suora",
	"Täyskäsi",
	"Sattuma",
	"Yazy",
)


CATEGORY_TO_KEY = {
	"Ykköset": "1s",
	"Kakkoset": "2s",
	"Kolmoset": "3s",
	"Neloset": "4s",
	"Viitoset": "5s",
	"Kuutoset": "6s",
	"Pari": "pair",
	"Kaksi paria": "2pair",
	"Kolme samaa": "3oak",
	"Neljä samaa": "4oak",
	"Pieni suora": "1-5",
	"Suuri suora": "2-6",
	"Täyskäsi": "FullH",
	"Sattuma": "misc",
	"Yazy": "yatzy",
}


class Scorecard:
	def __init__(self):
		self.scores = {
			"1s": None,
			"2s": None,
			"3s": None,
			"4s": None,
			"5s": None,
			"6s": None,
			"bonus": 0,
			"pair": None,
			"2pair": None,
			"3oak": None,
			"4oak": None,
			"1-5": None,
			"2-6": None,
			"FullH": None,
			"misc": None,
			"yatzy": None,
		}

	def _key_for_category(self, category: str) -> str:
		if category == "Yatzy":
			category = "Yazy"
		key = CATEGORY_TO_KEY.get(category)
		if key is None:
			raise ValueError(f"Unknown category: {category}")
		return key

	def available_categories(self) -> list[str]:
		return [category for category in CATEGORIES if self.get_score(category) is None]

	def get_score(self, category: str):
		return self.scores[self._key_for_category(category)]

	def record(self, category: str, points: int) -> None:
		key = self._key_for_category(category)
		if self.scores[key] is not None:
			raise ValueError(f"Category already used: {category}")
		self.scores[key] = int(points)
		self.scores["bonus"] = self.upper_bonus()

	def upper_total(self) -> int:
		total = 0
		for key in ("1s", "2s", "3s", "4s", "5s", "6s"):
			value = self.scores[key]
			if value is not None:
				total += value
		return total

	def upper_bonus(self) -> int:
		return 50 if self.upper_total() >= 63 else 0

	def total(self) -> int:
		total_points = 0
		for key, value in self.scores.items():
			if key != "bonus" and value is not None:
				total_points += value
		return total_points + self.upper_bonus()

	# Legacy compatibility helpers used by the current UI and older code.
	def validHands(self, dice: list[int]) -> list:
		counts = Counter(dice)
		n = [counts[i] for i in range(1, 7)]
		valid = []
		for category in self.available_categories():
			if category == "Sattuma" or calculate(category, dice) > 0:
				valid.append(category)
		return [valid, n]

	@property
	def vsumma(self) -> int:
		return self.upper_total()

	@property
	def summa(self) -> int:
		return self.total()

	def sheetFull(self) -> bool:
		for category in CATEGORIES:
			if self.get_score(category) is None:
				return False
		return True

	def printScores(self) -> None:
		for category in CATEGORIES:
			print(f"{category}:", self.get_score(category))
		print("Välisumma:", self.upper_total())
		print("Bonus:", self.upper_bonus())
		print("Summa:", self.total())