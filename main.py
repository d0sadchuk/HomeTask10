# #rock paper scissors lizard spock
import random

player_choice = ""
bot_choice = ""
player_score = 0
bot_score = 0
a = 0
# for i in range(1, 3 + 1):
start = str(input("to start game enter 'start', when you decide to finish enter 'finish' : "))
if start == "start":
    while True:
        a = a + 1
        print(f"round {a}")

        player_choice = str(input("enter [r], [p], [s], [l], [k] or [finish] : "))
        bot_choice = random.choice("rpslk")

        print(f"player choice : {player_choice}\nbot choice : {bot_choice} ")

        if player_choice == bot_choice:
            print("draw")
        elif player_choice == "s":
            if bot_choice == "p":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "r":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "l":
                print("player won")
                bot_score = bot_score + 1
            elif bot_choice == "k":
                print("bot won")
                player_score = player_score + 1

        elif player_choice == "r":
            if bot_choice == "p":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "s":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "l":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "k":
                print("bot won")
                bot_score = bot_score + 1

        elif player_choice == "p":
            if bot_choice == "r":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "s":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "l":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "k":
                print("player won")
                player_score = player_score + 1

        elif player_choice == "l":
            if bot_choice == "r":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "p":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "s":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "k":
                print("player won")
                player_score = player_score + 1

        elif player_choice == "k":
            if bot_choice == "r":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "p":
                print("bot won")
                bot_score = bot_score + 1
            elif bot_choice == "s":
                print("player won")
                player_score = player_score + 1
            elif bot_choice == "l":
                print("bot won")
                bot_score = bot_score + 1

        elif player_choice == "finish":
            print("game finished")
            if player_score == bot_score:
                print(f"draw, player has {player_score} equal score with bot {bot_score}")
            elif player_score > bot_score:
                print(f"player won, {player_score} > {bot_score}")
            elif player_score < bot_score:
                print(f"bot won, {player_score} < {bot_score}")
            break
        else:
            print("enter a valid command from a list: [p], [r], [s], [l], [k] or 'finish'")
elif start == "finish":
    print("see you next time")
else:
    print("please check command, to play you have to restart a game")
# if start == "finish":
#     print("see you next time")
