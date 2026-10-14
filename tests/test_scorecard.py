import unittest

from game.scorecard import Scorecard


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


class ScorecardTests(unittest.TestCase):
    def setUp(self):
        self.scorecard = Scorecard()

    def test_all_categories_are_available_at_start(self):
        # Bonus ei ole käytettävä kategoria, joten listassa on 15 pelattavaa kohtaa.
        self.assertCountEqual(self.scorecard.available_categories(), CATEGORIES)

    def test_score_can_be_recorded_and_read(self):
        self.scorecard.record("Ykköset", 3)

        # Tallennettu kategoria poistuu samalla käytettävissä olevista.
        self.assertEqual(self.scorecard.get_score("Ykköset"), 3)
        self.assertNotIn("Ykköset", self.scorecard.available_categories())

    def test_category_can_only_be_recorded_once(self):
        self.scorecard.record("Ykköset", 3)

        with self.assertRaises(ValueError):
            self.scorecard.record("Ykköset", 4)

    def test_unknown_category_is_rejected(self):
        with self.assertRaises(ValueError):
            self.scorecard.record("Tuntematon", 0)

    def test_upper_total_sums_upper_categories(self):
        for category, points in zip(CATEGORIES[:6], (3, 6, 9, 12, 15, 18)):
            self.scorecard.record(category, points)

        self.assertEqual(self.scorecard.upper_total(), 63)

    def test_upper_bonus_is_zero_below_threshold(self):
        # Yläosan yhteispisteet ovat tässä 62, eli yhden pisteen alle bonusrajan.
        for category, points in zip(CATEGORIES[:6], (3, 6, 9, 12, 15, 17)):
            self.scorecard.record(category, points)

        self.assertEqual(self.scorecard.upper_bonus(), 0)

    def test_upper_bonus_is_awarded_at_threshold(self):
        # Täsmälleen 63 yläosan pistettä antaa 50 pisteen bonuksen.
        for category, points in zip(CATEGORIES[:6], (3, 6, 9, 12, 15, 18)):
            self.scorecard.record(category, points)

        self.assertEqual(self.scorecard.upper_bonus(), 50)

    def test_total_includes_upper_bonus(self):
        # Kokonaissumma sisältää yläosan 63 pistettä, 50 pisteen bonuksen ja parin.
        for category, points in zip(CATEGORIES[:6], (3, 6, 9, 12, 15, 18)):
            self.scorecard.record(category, points)
        self.scorecard.record("Pari", 7)

        self.assertEqual(self.scorecard.total(), 120)

    def test_scorecard_sheetFull_only_after_all_categories_are_recorded(self):
        self.assertFalse(self.scorecard.sheetFull())

        # Nollakin on käytetty pistemäärä, joten kaikki kategoriat voidaan täyttää.
        for category in CATEGORIES:
            self.scorecard.record(category, 0)

        self.assertTrue(self.scorecard.sheetFull())


if __name__ == "__main__":
    unittest.main()