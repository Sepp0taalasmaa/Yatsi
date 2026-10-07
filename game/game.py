"""Game flow and turn orchestration."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from game.player import Player


class Game:
	def __init__(self, players: list[Player]) -> None:
		print("Pelaajat:")
		for player in players:
			print(f"- {player.nimi}")
		# TODO: Validate players and initialize dice, turn, and roll state.
		raise NotImplementedError

	@property
	def current_player(self) -> Player:
		# TODO: Return the player whose turn it is.
		raise NotImplementedError

	def roll_dice(self, mask: str = "11111") -> list[int]:
		# TODO: Roll selected dice and reject a fourth roll in the same turn.
		raise NotImplementedError

	def finish_turn(self, category: str) -> int:
		# TODO: Calculate and record points, then advance to the next player.
		raise NotImplementedError

	def is_finished(self) -> bool:
		# TODO: Return whether every player's scorecard is complete.
		raise NotImplementedError

	def winners(self) -> list[Player]:
		# TODO: Return all highest-scoring players after the game is complete.
		raise NotImplementedError