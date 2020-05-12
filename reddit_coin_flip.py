import random
import time

score = {
    "player": 0,
    "computer": 0,
}
player_turn = True


def flip_coin():
    values = ["heads", "tails"]
    return random.choice(values)


def cpu_turn():
    values = ["heads", "tails"]
    return random.choice(values)


def get_player_choice():
    return input("Heads or Tails? ").lower()


def update_score(player, player_choice, coin_value):
    if player_choice == coin_value:
        score[player] += 1
    print(f"{player} picked {player_choice}, the coin is {coin_value}! {player} has a score of {score[player]}")


def game_round():
    global player_turn
    if player_turn:
        print("Your turn!")
        player = "player"
        choice = get_player_choice()
    else:
        print("Computers turn!")
        time.sleep(1)
        player = "computer"
        choice = cpu_turn()

    coin_value = flip_coin()
    update_score(player, choice, coin_value)
    player_turn = not player_turn


def game_over():
    print("Game Over")
    print(score)
    exit()


def start_game():
    while score["player"] < 5 and score["computer"] < 5:
        game_round()
    else:
        game_over()


if __name__ == "__main__":
    start_game()
