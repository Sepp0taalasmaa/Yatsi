from game.player import Player
from game.scorecard import Scorecard
from game.dice import Dice

class UI:

    def run(self, game):
        while not game.is_finished():
            player = game.current_player
            print(f"\nVuorossa: {player.name}")
            self.show_scorecard(player)

            values = game.roll_dice()
            for roll_number in range(1, 3):
                print(f"\nHeitto {roll_number}/3")
                mask = self.read_dice_mask(values)
                if mask == "00000":
                    break
                values = game.roll_dice(mask)

            categories = player.scorecard.validHands(values)[0]
            category = self.read_category(categories)
            points = game.finish_turn(category)
            print(f"{points} pistettä kategoriasta {category}.")

        winners = game.winners()
        if len(winners) == 1:
            print(f"\nVoittaja: {winners[0].name} ({winners[0].total_score()} pistettä)")
        else:
            names = ", ".join(player.name for player in winners)
            print(f"\nTasapeli: {names}")

    def read_dice_mask(self, values: list[int]) -> str:
        print("Nopat:")

        for i, value in enumerate(values, 1):
            print(f"{i}: [{value}]")

        while True:
            mask = input("Heitettävät nopat (1/0, 00000 lopettaa): ")

            if len(mask) == 5 and all(x in "01" for x in mask):
                return mask

            print("Virheellinen syöte.")

    def read_category(self, categories: list[str]) -> str:
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


def run(game) -> None:
    UI().run(game)



