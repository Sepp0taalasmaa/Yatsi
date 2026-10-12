import unittest
from unittest.mock import patch

from game.dice import Dice


class DiceTests(unittest.TestCase):
    @patch("game.dice.randint", side_effect=[1, 2, 3, 4, 5])
    def test_roll_without_selector_rolls_all_dice(self, randint_mock):
        # Kiinteät noppa-arvot tekevät satunnaisesta heitosta toistettavan.
        dice = Dice()

        dice.roll()

        self.assertEqual(dice.vals, [1, 2, 3, 4, 5])
        self.assertEqual(randint_mock.call_count, 5)

    @patch("game.dice.randint", side_effect=[1, 2, 3])
    def test_roll_only_changes_selected_dice(self, randint_mock):
        dice = Dice()
        dice.vals = [6, 5, 4, 3, 2]

        # Maski 01011 heittää nopat 2, 4 ja 5; muut arvot säilyvät.
        dice.roll("01011")

        self.assertEqual(dice.vals, [6, 1, 4, 2, 3])
        self.assertEqual(randint_mock.call_count, 3)

    def test_roll_rejects_selector_with_wrong_length(self):
        dice = Dice()

        # Maskissa pitää olla yksi merkki kutakin viittä noppaa kohti.
        with self.assertRaises(ValueError):
            dice.roll("1111")

    def test_roll_rejects_non_binary_selector(self):
        dice = Dice()

        # Sallittuja merkkejä ovat vain 0 (säilytä) ja 1 (heitä).
        with self.assertRaises(ValueError):
            dice.roll("10x01")


if __name__ == "__main__":
    unittest.main()