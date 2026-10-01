
import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

computer = random.choice([1, 0, -1])

youstr = input("Enter your choice: s for Snake, g for Gun, w for Water: ")

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

younum = youDict[youstr]

print(f"Computer chose: {reverseDict[computer]}")
print(f"You chose: {reverseDict[younum]}")

if computer == younum:
    print("Draw")

else:
    if computer == -1 and younum == 1:
        print("You Win")

    elif computer == -1 and younum == 0:
        print("You Lose")

    elif computer == 1 and younum == -1:
        print("You Lose")

    elif computer == 1 and younum == 0:
        print("You Win")

    elif computer == 0 and younum == -1:
        print("You Win")

    elif computer == 0 and younum == 1:
        print("You Lose")

    else:
        print("Something went wrong!!")
