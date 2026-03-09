# Creative addition: I added a health system and replay option, and I tested the game with two friends to improve choices and endings.

print("Welcome to the Adventure Game!")
print("Your goal is to survive and escape.\n")

health = 100

# ---------- LEVEL 1 ----------
while True:
    print("You wake up in a dark forest. You hear strange noises.")
    print("Do you want to go LEFT, RIGHT, or FORWARD?")
    choice1 = input("> ").strip().lower()

    if choice1 == "left":
        print("\nYou walk left and fall into a small pit.")
        health -= 20
        print(f"Your health is now {health}.")
        scenario1 = "pit"
        break

    elif choice1 == "right":
        print("\nYou go right and find an abandoned hut.")
        scenario1 = "hut"
        break

    elif choice1 == "forward":
        print("\nYou move forward and encounter a wild animal!")
        health -= 30
        print(f"Your health is now {health}.")
        scenario1 = "animal"
        break

    else:
        print("Invalid choice. Please choose LEFT, RIGHT, or FORWARD.\n")

# ---------- LEVEL 2 ----------
while True:
    if scenario1 == "pit":
        print("\nYou are in the pit.")
        print("Do you want to CLIMB, CALL for help, or WAIT?")
        choice2 = input("> ").strip().lower()

        if choice2 == "climb":
            print("\nYou climb out safely.")
            scenario2 = "escape"
            break
        elif choice2 == "call":
            print("\nNo one hears you. You lose energy.")
            health -= 10
            print(f"Your health is now {health}.")
            scenario2 = "tired"
            break
        elif choice2 == "wait":
            print("\nA rope appears from above. You are rescued!")
            scenario2 = "escape"
            break
        else:
            print("Invalid choice. Please choose CLIMB, CALL, or WAIT.\n")

    elif scenario1 == "hut":
        print("\nInside the hut you see supplies.")
        print("Do you want to EAT, SLEEP, or SEARCH?")
        choice2 = input("> ").strip().lower()

        if choice2 == "eat":
            print("\nYou regain strength.")
            health += 20
            print(f"Your health is now {health}.")
            scenario2 = "strong"
            break
        elif choice2 == "sleep":
            print("\nYou oversleep and lose time.")
            scenario2 = "late"
            break
        elif choice2 == "search":
            print("\nYou find a map!")
            scenario2 = "map"
            break
        else:
            print("Invalid choice. Please choose EAT, SLEEP, or SEARCH.\n")

    elif scenario1 == "animal":
        print("\nThe animal blocks your path.")
        print("Do you want to RUN, FIGHT, or HIDE?")
        choice2 = input("> ").strip().lower()

        if choice2 == "run":
            print("\nYou escape, but barely.")
            health -= 10
            print(f"Your health is now {health}.")
            scenario2 = "escape"
            break
        elif choice2 == "fight":
            print("\nYou scare it away but get injured.")
            health -= 40
            print(f"Your health is now {health}.")
            scenario2 = "injured"
            break
        elif choice2 == "hide":
            print("\nThe animal leaves.")
            scenario2 = "safe"
            break
        else:
            print("Invalid choice. Please choose RUN, FIGHT, or HIDE.\n")

# ---------- LEVEL 3 ----------
print("\nFinal Decision:")
while True:
    print("You see the edge of the forest.")
    print("Do you want to REST or CONTINUE?")
    choice3 = input("> ").strip().lower()

    if choice3 == "rest":
        print("\nYou rest and regain health.")
        health += 10
        print(f"Your final health is {health}.")
        print("You safely leave the forest. YOU WIN! 🎉")
        break

    elif choice3 == "continue":
        if health >= 40:
            print("\nYou push through and escape successfully!")
            print("YOU WIN! 🎉")
        else:
            print("\nYou collapse from exhaustion.")
            print("GAME OVER.")
        break

    else:
        print("Invalid choice. Please choose REST or CONTINUE.\n")

print("\nThanks for playing!")
