"""Pure scoring rules for Yatsi categories."""

from collections import Counter


def _validate_dice(dice: list[int]) -> None:
	if len(dice) != 5:
		raise ValueError("Dice must contain exactly five values.")
	for value in dice:
		if not isinstance(value, int) or not 1 <= value <= 6:
			raise ValueError("Each die must be an integer from 1 to 6.")


def calculate(category: str, dice: list[int]) -> int:
	"""Return score for a category and five dice values.

	This function is side-effect free and does not modify any game state.
	"""
	_validate_dice(dice)
	counts = Counter(dice)
	sorted_values = sorted(dice)

	upper = {
		"Ykköset": 1,
		"Kakkoset": 2,
		"Kolmoset": 3,
		"Neloset": 4,
		"Viitoset": 5,
		"Kuutoset": 6,
	}
	if category in upper:
		face = upper[category]
		return counts[face] * face

	if category == "Pari":
		for face in range(6, 0, -1):
			if counts[face] >= 2:
				return face * 2
		return 0

	if category == "Kaksi paria":
		pairs = [face for face in range(6, 0, -1) if counts[face] >= 2]
		if len(pairs) >= 2:
			return pairs[0] * 2 + pairs[1] * 2
		return 0

	if category == "Kolme samaa":
		for face in range(6, 0, -1):
			if counts[face] >= 3:
				return face * 3
		return 0

	if category == "Neljä samaa":
		for face in range(6, 0, -1):
			if counts[face] >= 4:
				return face * 4
		return 0

	if category == "Pieni suora":
		return 15 if sorted_values == [1, 2, 3, 4, 5] else 0

	if category == "Suuri suora":
		return 20 if sorted_values == [2, 3, 4, 5, 6] else 0

	if category == "Täyskäsi":
		occurrences = sorted(counts.values())
		return sum(dice) if occurrences == [2, 3] else 0

	if category == "Sattuma":
		return sum(dice)

	if category in ("Yazy", "Yatzy"):
		return 50 if len(counts) == 1 else 0

	raise ValueError(f"Unknown category: {category}")