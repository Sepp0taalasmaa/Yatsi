"""Game flow and turn orchestration."""

from __future__ import annotations

from game.dice import Dice
from game.player import Player


class Game:
	def __init__(self, players: list[Player]) -> None:
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
		return "A"

		# TODO: Return the player whose turn it is.


	def roll_dice(self, mask: str = "11111") -> list[int]:
		# TODO: Roll selected dice and reject a fourth roll in the same turn.
		raise NotImplementedError

	def finish_turn(self, category: str) -> int:
		# TODO: Calculate and record points, then advance to the next player.
		raise NotImplementedError

	def is_finished(self) -> bool:
		# TODO: Return whether every player's scorecard is complete.
		for player in self.players:
			if not player.scorecard.is_complete():
				return False
		return True

	def winners(self) -> list[Player]:
		# TODO: Return all highest-scoring players after the game is complete.
		raise NotImplementedError