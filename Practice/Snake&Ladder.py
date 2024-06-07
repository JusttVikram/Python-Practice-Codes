import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    position = 0

    while position < 100:
        dice_value = roll_dice()
        position += dice_value

        if position > 100:
            position -= dice_value

        print("You rolled a", dice_value)
        print("Your current position is", position)

        if position == 100:
            print("Congratulations! You won!")
            break

        if position == 4:
            position = 14
            print("Congratulations! You landed on a ladder. You are now at position 14.")
        elif position == 3:
            position = 22
            print("Oops! You landed on a snake. You are now at position 22.")
        elif position == 8:
            position = 37
            print("Oops! You landed on a snake. You are now at position 37.")
        elif position == 18:
            position = 9
            print("Oops! You landed on a snake. You are now at position 9.")
        elif position == 26:
            position = 47
            print("Oops! You landed on a snake. You are now at position 47.")
        elif position == 38:
            position = 60
            print("Oops! You landed on a snake. You are now at position 60.")
        elif position == 45:
            position = 17
            print("Oops! You landed on a snake. You are now at position 17.")
        elif position == 52:
            position = 81
            print("Oops! You landed on a ladder. You are now at position 81.")
        elif position == 76:
            position = 97
            print("Oops! You landed on a ladder. You are now at position 97.")
        elif position == 88:
            position = 36
            print("Oops! You landed on a snake. You are now at position 36.")
        elif position == 91:
            position = 72
            print("Oops! You landed on a snake. You are now at position 72.")
        elif position == 94:
            position = 42
            print("Oops! You landed on a snake. You are now at position 42.")
        elif position == 99:
            position = 7
            print("Oops! You landed on a snake. You are now at position 7.")

play_game()