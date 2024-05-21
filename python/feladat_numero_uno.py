szam = int(input("Írj be egy számot:"))
osztok = 0
for i in range(1, szam+1):
    if szam % i == 0:
        osztok += 1
    else:
        pass
if szam == 1:
    print("Nem prím.")
elif osztok < 3:
    print("Prím.")
else:
    print("Nem prím.")
