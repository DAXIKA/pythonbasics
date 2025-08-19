import random
tablazat = [[1, "rock", "paper"], [0, "rock", "scissors"], [-1, "rock", "rock"], [0, "paper", "rock"], [1, "paper",
                                                                                          "scissors"], [-1, "paper", "paper"], [-1, "scissors", "scissors"], [1, "scissors", "rock"], [0, "scissors", "paper"]]


def find(a: str, b: str, i: list):
    for k in i:
        if a == k[1] and b == k[2]:
            return k[0]

    # raise Exception("valami nagyon nem jó")
cuccok: list = ["rock", "paper", "scissors"]
user: str = input(f"Enter your choice ({"/".join(cuccok)}): ")
if user in cuccok:
    randomcucc: str = cuccok[random.randint(1, 3)-1]
    print("\n\n-------\n",
          f"Your choice: {user}\n", f"Computer's choice: {randomcucc}")
    index: int = find(user, randomcucc, tablazat)
    if index == 0:
        print(" You won")
    elif index == 1:
        print(" The computer won")
    elif index == -1:
        print(" It's a draw")
    else:
        print(" Something is very wrong!!!")
    print("-------\n\n")
else:
    print("You must provide a valid option!!")
