import unittest

from scoring.scoring import calculate


class ScoringTests(unittest.TestCase):
    def test_upper_categories(self):
        # Jokaisessa tapauksessa laskettava silmäluku esiintyy nopissa kahdesti.
        cases = (
            ("Ykköset", [1, 1, 2, 3, 4], 2),
            ("Kakkoset", [2, 2, 1, 3, 4], 4),
            ("Kolmoset", [3, 3, 1, 2, 4], 6),
            ("Neloset", [4, 4, 1, 2, 3], 8),
            ("Viitoset", [5, 5, 1, 2, 3], 10),
            ("Kuutoset", [6, 6, 1, 2, 3], 12),
        )

        for category, dice, expected in cases:
            with self.subTest(category=category):
                self.assertEqual(calculate(category, dice), expected)

    def test_matching_combinations(self):
        # Parit, samanarvoiset nopat, suorat ja erikoisyhdistelmät.
        cases = (
            ("Pari", [2, 2, 1, 3, 5], 4),
            ("Kaksi paria", [1, 1, 4, 4, 6], 10),
            ("Kolme samaa", [3, 3, 3, 1, 6], 9),
            ("Neljä samaa", [4, 4, 4, 4, 1], 16),
            ("Pieni suora", [1, 2, 3, 4, 5], 15),
            ("Suuri suora", [2, 3, 4, 5, 6], 20),
            ("Täyskäsi", [2, 2, 3, 3, 3], 13),
            ("Sattuma", [1, 2, 3, 4, 5], 15),
            ("Yazy", [6, 6, 6, 6, 6], 50),
        )

        for category, dice, expected in cases:
            with self.subTest(category=category):
                self.assertEqual(calculate(category, dice), expected)

    def test_nonmatching_valid_hand_scores_zero(self):
        # Nopat ovat kelvollisia, mutta ne eivät muodosta Yazy-yhdistelmää.
        self.assertEqual(calculate("Yazy", [1, 1, 1, 1, 2]), 0)

    def test_combination_score_does_not_depend_on_dice_order(self):
        # Sama pieni suora pisteytetään samalla tavalla missä järjestyksessä tahansa.
        self.assertEqual(calculate("Pieni suora", [1, 2, 3, 4, 5]), 15)
        self.assertEqual(calculate("Pieni suora", [5, 3, 1, 4, 2]), 15)

    def test_unknown_category_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate("Tuntematon", [1, 2, 3, 4, 5])

    def test_invalid_dice_are_rejected(self):
        # Arvon 0, arvon 6 ylitys ja väärä määrä noppia ovat virheellisiä.
        for dice in ([0, 2, 3, 4, 5], [1, 2, 3, 4, 7], [1, 2, 3, 4]):
            with self.subTest(dice=dice):
                with self.assertRaises(ValueError):
                    calculate("Sattuma", dice)


if __name__ == "__main__":
    unittest.main()