import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


p1 = Player(1)
p2 = Player(2)


def start():

    minimum = int(input("\nLet's pick a number range for our game.\n What is the minimum number?: "))
    maximum = int(input("And what is the maximum number? "))
    while maximum < minimum:
        maximum = int(
            input("The max cannot be less than the minimum: {}.\n What is the maximum number? ".format(minimum)))
    p1.name = input("\nWhat is your name player 1? ")
    p2.name = input("What is your name player 2? ")

    num = random.randint(minimum, maximum)
    guess = 0
    guess2 = 0

    wrong = []
    wrong2 = []

    while (int(guess) | int(guess2)) != num:
        if wrong:
            print("\n{}, so far you have guessed: {}".format(p1.name, wrong))
        guess = input("{}, guess a number from {} to {}: ".format(p1.name, minimum, maximum))
        guess = int(guess)

        while guess > maximum:
            print("That number is too high!")
            guess = int(input("\nTry another number, {}: ".format(p1.name)))

        while guess < minimum:
            print("That number is too low!")
            guess = int(input("\nTry another number, {}: ".format(p1.name)))
        wrong.append(guess)

        if wrong2:
            print("{}, so far you have guessed: {}".format(p2.name, wrong2))
        guess2 = input("{}, guess a number from {} to {}: ".format(p2.name, minimum, maximum))
        guess2 = int(guess2)

        while guess2 > maximum:
            print("That number is too high!")
            guess2 = int(input("\nTry another number, {}: ".format(p2.name)))

        while guess2 < minimum:
            print("That number is too low!")
            guess = int(input("\nTry another number, {}: ".format(p2.name)))
        wrong2.append(guess2)

        if guess == num and guess2 == num:
            print("\nCongrats, you both got it right!\n The number was: {}".format(num))
            break
        if guess == num:
            print("\nCongratulations! You won, {} :)!\n The number was: {}".format(p1.name, num))
            p1.score += 1
            print("The score is now:\n {}: {} \n {}: {}".format(p1.name, p1.score, p2.name, p2.score))
            break
        if guess2 == num:
            print("\nCongratulations! You won, {}!\n The number was: {}!".format(p2.name, num))
            p2.score += 1
            print("The score is now:\n {}: {} \n {}: {}".format(p1.name, p1.score, p2.name, p2.score))
            break
        else:
            print("Sorry, Try again you two!")

    print("That was fun!")

    new_game = None
    while new_game not in ['y', 'yes', 'n', 'no']:
        new_game = input("Would you like to play again? Y/N: ").lower()
        if new_game == "y" or new_game == "yes":
            return start()
        elif new_game == "n" or new_game == "no":
            print("Thank you for playing!")
        else:
            print("Please enter a valid response. \n ")


start()
