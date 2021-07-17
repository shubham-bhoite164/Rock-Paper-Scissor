import random


lappy_wins = 0
player_wins = 0

# Now Generate the function for user to select the one

def choose_opetion():
    player_choice  = input("Choose Rock, Paper or Scissor: ")

    if player_choice in ["Rock","rock","R","r"]:
        player_choice = "r"

    elif player_choice in ["Paper","paper","P","p"]:
        player_choice = "p"

    elif player_choice in ["Scissor", "scissor", "S", "s"]:
        player_choice = "s"

    else:
        print("I don't Understand please try again. ")

    return player_choice

def lappy_opetion():
    lappy_choice = random.randint(1,3)

    if lappy_choice == 1:
        lappy_choice = "r"
        print("Computer has choosen Rock")

    elif lappy_choice == 2:
        lappy_choice = "p"
        print("Computer has choosen Paper")

    elif lappy_choice == 3:
        lappy_choice = "s"
        print("Computer has choosen Scissor")

    return lappy_choice

while True:
    print("")
    player_choice = choose_opetion()
    lappy_choice = lappy_opetion()
    print("")

    if player_choice == "r":
        if lappy_choice == "r":
            print("You choose rock. The computer choose rock. You tied")

        elif lappy_choice == "p":
            print("You choose rock. The computer choose paper. You lose")

        elif lappy_choice == "s":
            print("You choose rock. The computer choose scissor. You win")

    elif player_choice == "p":
        if lappy_choice == "r":
            print("You choose paper. The computer choose rock. You win")

        elif lappy_choice == "p":
            print("You choose paper. The computer choose paper. You tied")

        elif lappy_choice == "s":
            print("You choose paper. The computer choose scissor. You lose")

    elif player_choice == "s":
        if lappy_choice == "r":
            print("You choose scissor. The computer choose rock. You lose")

        elif lappy_choice == "p":
            print("You choose scissor. The computer choose paper. You win")

        elif lappy_choice == "s":
            print("You choose scissor. The computer choose scissor. You tied")

    print("")
    print("player wins : " + str(player_wins))
    print("lappy wins :" + str(lappy_wins))
    print("")

    player_choice = input("Do you want to play again?  (y/n)")
    if player_choice in ["Y", "y", "Yes", "yes"]:
        pass
    elif player_choice in ["N", "n", "No", "no"]:
        break
    else:
        break



