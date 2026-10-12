"""Game-luokan tavoiteltu toiminta README:n rajapinnan mukaan."""

import unittest
from unittest.mock import Mock, patch

from game.dice import Dice
from game.game import Game
from game.player import Player


class GameTests(unittest.TestCase):
    def setUp(self):
        # Pistetaulukon keskeneräinen toteutus ei vaikuta Game-yksikkötesteihin.
        self.players = [Player("Matti"), Player("Maija")]
        for player in self.players:
            player._scorecard = Mock()
            player.scorecard.is_complete.return_value = False
        self.print_patch = patch("builtins.print")
        self.print_patch.start()
        self.addCleanup(self.print_patch.stop)
        self.game = Game(self.players)

    def test_initializes_dice_and_counters(self):
        self.assertIsInstance(self.game.dice, Dice)
        self.assertEqual(self.game.dice.vals, [0, 0, 0, 0, 0])
        self.assertEqual(self.game.turn, 0)
        self.assertEqual(self.game.rolls, 0)

    def test_games_have_independent_dice(self):
        other = Game(self.players)
        self.game.dice.vals[0] = 6
        self.assertEqual(other.dice.vals, [0, 0, 0, 0, 0])

    def test_rejects_empty_player_list(self):
        with self.assertRaises(ValueError):
            Game([])

    def test_first_player_starts(self):
        self.assertIs(self.game.current_player, self.players[0])

    def test_single_player_can_start(self):
        game = Game([self.players[0]])
        self.assertIs(game.current_player, self.players[0])

    @patch("game.dice.randint", side_effect=[1, 2, 3, 4, 5])
    def test_rolls_all_dice_and_counts_roll(self, randint_mock):
        self.assertEqual(self.game.roll_dice(), [1, 2, 3, 4, 5])
        self.assertEqual(self.game.rolls, 1)
        self.assertEqual(randint_mock.call_count, 5)

    @patch("game.dice.randint", side_effect=[1, 2, 3, 4, 5, 6, 6])
    def test_rerolls_only_selected_dice(self, randint_mock):
        self.game.roll_dice()
        self.assertEqual(self.game.roll_dice("01010"), [1, 6, 3, 6, 5])
        self.assertEqual(self.game.rolls, 2)
        self.assertEqual(randint_mock.call_count, 7)

    @patch("game.dice.randint", return_value=3)
    def test_roll_returns_copy_of_values(self, randint_mock):
        values = self.game.roll_dice()
        values[0] = 6
        self.assertEqual(self.game.dice.vals, [3, 3, 3, 3, 3])

    @patch("game.dice.randint", return_value=3)
    def test_fourth_roll_is_rejected_without_changing_state(self, randint_mock):
        for _ in range(3):
            self.game.roll_dice()
        before = self.game.dice.vals.copy()
        with self.assertRaises(ValueError):
            self.game.roll_dice()
        self.assertEqual(self.game.rolls, 3)
        self.assertEqual(self.game.dice.vals, before)
        self.assertEqual(randint_mock.call_count, 15)

    def test_invalid_mask_is_rejected(self):
        for mask in ("1111", "111111", "x1111"):
            with self.subTest(mask=mask):
                with self.assertRaises(ValueError):
                    self.game.roll_dice(mask)
                self.assertEqual(self.game.rolls, 0)

    @patch("game.dice.randint", side_effect=[1, 2, 3, 4, 5])
    def test_finish_turn_records_points_and_advances_player(self, randint_mock):
        self.game.roll_dice()
        points = self.game.finish_turn("Sattuma")
        self.assertEqual(points, 15)
        self.players[0].scorecard.record.assert_called_once_with("Sattuma", 15)
        self.players[1].scorecard.record.assert_not_called()
        self.assertIs(self.game.current_player, self.players[1])
        self.assertEqual(self.game.rolls, 0)

    @patch("game.dice.randint", return_value=3)
    def test_turn_wraps_back_to_first_player(self, randint_mock):
        for _ in self.players:
            self.game.roll_dice()
            self.game.finish_turn("Sattuma")
        self.assertIs(self.game.current_player, self.players[0])
        self.assertEqual(self.game.rolls, 0)
        self.game.roll_dice()
        self.assertEqual(self.game.rolls, 1)

    def test_new_game_is_not_finished(self):
        self.assertFalse(self.game.is_finished())

    def test_one_complete_scorecard_does_not_finish_game(self):
        self.players[0].scorecard.is_complete.return_value = True
        self.assertFalse(self.game.is_finished())

    def test_all_complete_scorecards_finish_game(self):
        for player in self.players:
            player.scorecard.is_complete.return_value = True
        self.assertTrue(self.game.is_finished())

    def test_no_winners_before_game_finishes(self):
        self.assertEqual(self.game.winners(), [])

    def test_highest_scoring_player_wins(self):
        for player, score in zip(self.players, [100, 150]):
            player.scorecard.is_complete.return_value = True
            player.total_score = Mock(return_value=score)
        self.assertEqual(self.game.winners(), [self.players[1]])

    def test_tied_players_both_win(self):
        for player in self.players:
            player.scorecard.is_complete.return_value = True
            player.total_score = Mock(return_value=150)
        self.assertCountEqual(self.game.winners(), self.players)


if __name__ == "__main__":
    unittest.main()
