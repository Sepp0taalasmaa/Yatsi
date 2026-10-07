from game.game import Game
from game.player import Player
from ui.console_ui import run


def create_players() -> list[Player]:
    while True:
        try:
            player_count = int(input("Pelaajien määrä: "))
            if player_count > 0:
                break
            print("Pelaajia pitää olla vähintään yksi.")
        except ValueError:
            print("Anna pelaajien määrä numerona.")

    players = []
    for number in range(1, player_count + 1):
        name = input(f"Pelaajan {number} nimi: ").strip()
        players.append(Player(name or f"Pelaaja {number}"))
    return players


def main() -> None:
    game = Game(create_players())
    run(game)


if __name__ == "__main__":
    main()