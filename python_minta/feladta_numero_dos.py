from random import randint
bor = 0
reszeg = False
for i in range(1, 31):
    if reszeg == False:
        bor += randint(1,10)
        random = randint(1, 5)
        if random == 1:
            bor -= 3
            reszeg = True
        print(f"{i}. nap: {bor} literje van")
    elif reszeg == True:
        print(f"{i}. nap: Jani bácsi másnapos, nem főzött ma")
        reszeg = False
    else:
        reszeg = False
print(f"Jani bácsinak {bor} liter borja lett")