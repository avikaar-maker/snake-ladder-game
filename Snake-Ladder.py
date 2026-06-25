# THIS IS A SNAKE AND LADDER GAME MADE BY ME FOR LEARNING PURPOSE.
import random
# Snakes and ladders positions
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}


def roll_dice():
    return random.randint(1, 6)


def move_player(position, dice):
    position += dice

    if position > 100:
        return position - dice

    if position in snakes:
        print(f"Snake! Go down to {snakes[position]}")
        position = snakes[position]

    elif position in ladders:
        print(f" Ladder! Climb up to {ladders[position]}")
        position = ladders[position]

    return position


player1 = 0
player2 = 0

print(" Welcome to Snake and Ladder ")

while True:
    input("\nPlayer 1 - Press Enter to roll dice...")
    dice = roll_dice()
    print(f"Player 1 rolled: {dice}")

    player1 = move_player(player1, dice)
    print(f"Player 1 Position: {player1}")

    if player1 == 100:
        print("\n🏆 Player 1 Wins!")
        print("CONGRATULATIONS")
        break

    input("\nPlayer 2 - Press Enter to roll dice...")
    dice = roll_dice()
    print(f"Player 2 rolled: {dice}")

    player2 = move_player(player2, dice)
    print(f"Player 2 Position: {player2}")

    if player2 == 100:
        print("\n🏆 Player 2 Wins!")
        print("CONGRATULATIONS")
        break