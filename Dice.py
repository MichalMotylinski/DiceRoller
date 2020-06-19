import random


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def begin_game():
    print("Please provide number of players")
    player_num = int(input())
    players = []
    dice_min = 1
    round = 1
    winning_player = ""
    highest_score = 0

    for i in range(player_num):
        print("Please provide name of a Player " + str(i+1))
        player_name = input()
        player = Player(player_name, 0)
        players.append(player)

    print("How big dice?")
    dice_max = input()

    print("What maximum score?")
    max_score = int(input())

    print("Picking starting player randomly...")
    rolling_player = random.choice(players).name
    print("Player " + rolling_player + " starts the game")

    while highest_score < max_score:
        print("Round: " + str(round))

        throw(players, rolling_player, dice_min, int(dice_max))

        highest_score = max(player.score for player in players)
        for player in players:
            if player.score == highest_score:
                winning_player = player.name
                break
        print("End of round " + str(round) + ". " + winning_player + " is winning with " + str(highest_score))
        round += 1
        print("Press enter to play next round.")
        enter = input()

    print(winning_player + " won with score: " + str(highest_score))


def throw(players, current_player, dice_min, dice_max):
    for player in players:
        if player.name == current_player:
            current_roll = random.randint(dice_min, dice_max)
            player.score += current_roll
            print(player.name + " rolled: " + str(current_roll))
            current_player = player_change(players, current_player)


def player_change(players, current_player):
    player_index = 0
    for idx, player in enumerate(players):
        if player.name == current_player:
            player_index = idx

    if player_index < len(players)-1:
        next_player = players[player_index + 1].name
    else:
        next_player = players[0].name
    return next_player

begin_game()

"""player1 = "Player 1"
player2 = "Player 2"

player_1_score = 0
player_2_score = 0
current_round = 1

dice_min = 1
dice_max = 6

start_player = random.choice([player1, player2])
next_player = ""
print("Player " + start_player + " starts the game")


while player_1_score < 20 and player_2_score < 20:

    print("Round: " + str(current_round))
    if round == 1:
        current_score, current_player = throw(start_player)
        if current_player == player1:
            player_1_score += current_score
            next_player = player2
        else:
            player_2_score += current_score
            next_player = player1

    else:
        current_score, current_player = throw(next_player)
        if current_player == player1:
            player_1_score += current_score
            next_player = player2
        else:
            player_2_score += current_score
            next_player = player1
    print("Player 1 score: " + str(player_1_score))
    print("Player 2 score: " + str(player_2_score))
    current_round += 1"""


