from random import randint
bor = 0
random = 0
reszeg = False
for i in range(1, 31):
    if reszeg == False:
        bor += 5
        random += 1
        if random == 4:
            bor -= 3
            reszeg = True
            random = 0
        print(f"{i}. nap: {bor} literje van")
    elif reszeg == True:
        print(f"{i}. nap: Jani bácsi másnapos, nem főzött ma")
        reszeg = False
    else:
        reszeg = False
print(f"Jani bácsinak {bor} liter borja lett")