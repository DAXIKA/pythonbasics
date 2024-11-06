import random
tablazat = [[1, "kő", "papír"], [0, "kő", "olló"], [-1, "kő", "kő"], [0, "papír", "kő"], [1, "papír",
                                                                                          "olló"], [-1, "papír", "papír"], [-1, "olló", "olló"], [1, "olló", "kő"], [0, "olló", "papír"]]


def find(a: str, b: str, i: list):
    for k in i:
        if a == k[1] and b == k[2]:
            return k[0]

    # raise Exception("valami nagyon nem jó")
cuccok: list = ["k ő", "papír", "olló"]
user: str = input(f"Addja meg amit választott ({"/".join(cuccok)}): ")
if user in cuccok:
    randomcucc: str = cuccok[random.randint(1, 3)-1]
    print("\n\n-------\n",
          f"választásom: {user}\n", f"Gép választása: {randomcucc}")
    index: int = find(user, randomcucc, tablazat)
    if index == 0:
        print(" Én nyertem")
    elif index == 1:
        print(" A gép nyert")
    elif index == -1:
        print(" Döntetlen lett")
    else:
        print(" nagyon nagy baj van!!!")
    print("-------\n\n")
else:
    print("Valami értelmess opciót kell megadni!!")
