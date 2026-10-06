from game.player import Player
from game.scorecard import Scorecard
from game.dice import Dice

class UI:

    def read_dice_mask(self, dice: Dice):
        print("Nopat:")

        for i, value in enumerate(dice.vals, 1):
            print(f"{i}: [{value}]")

        while True:
            mask = input("Heitettävät nopat (1/0): ")

            if len(mask) == 5 and all(x in "01" for x in mask):
                return mask

            print("Virheellinen syöte.")

    def read_category(self, scorecard: Scorecard, dice: Dice):
        categories = scorecard.validHands(dice.vals)[0]

        print("\nValitse kategoria:")

        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        while True:
            try:
                choice = int(input("> "))

                if 1 <= choice <= len(categories):
                    return categories[choice - 1]

            except ValueError:
                pass

            print("Virheellinen valinta.")

    def show_scorecard(self, player: Player):
        player.scorecard.printScores()
