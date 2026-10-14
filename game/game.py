"""Game flow and turn orchestration."""

from __future__ import annotations

from game.dice import Dice
from game.player import Player
from scoring.scoring import calculate


class Game:
	def __init__(self, players: list[Player]) -> None:
		if not players:
			raise ValueError("At least one player is required.")
		self.players = players
		print("Pelaajat:")
		for player in players:
			print(f"- {player.nimi}")
		self.dice = Dice()
		print(self.dice.vals)
		self.turn = 0
		self.rolls = 0
		# TODO: Validate players and initialize dice, turn, and roll state.


	@property
	def current_player(self) -> Player:
		return self.players[self.turn]

		# TODO: Return the player whose turn it is.


	def roll_dice(self, mask: str = "11111") -> list[int]:
		if self.rolls >= 3:
			raise ValueError("A player can roll at most three times per turn.")
		self.dice.roll(mask)
		self.rolls += 1
		return self.dice.vals.copy()

	def finish_turn(self, category: str) -> int:
		points = calculate(category, self.dice.vals)
		self.current_player.scorecard.record(category, points)
		self.turn = (self.turn + 1) % len(self.players)
		self.rolls = 0
		return points

	def is_finished(self) -> bool:
		# TODO: Return whether every player's scorecard is complete.
		for player in self.players:
			if not player.scorecard.sheetFull():
				return False
		return True

	def winners(self) -> list[Player]:
		if not self.is_finished():
			return []

		best_score = max(player.total_score() for player in self.players)
		return [player for player in self.players if player.total_score() == best_score]