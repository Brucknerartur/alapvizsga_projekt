class Jatek:
    def __init__(self, row:str) -> None:
        splitted = row.strip().split(";")
        self.nev = splitted[0]
        self.datum = int(splitted[1])
        self.mufaj = splitted[2]
        self.ertekeles = int(splitted[3])

jatekok:list[Jatek] = []

def main():
    beolvas("python/games.csv")
    print(f"3. feladat: {len(jatekok)}")
    print(f"4. feladat: {jatekok[-1].nev}")
    akciojatekok = akcio_jatekok()
    print(f"5. feladat:")
    for a in akciojatekok:
        print(f"\t Név: {a.nev}, Kiadás dátuma: {a.datum}, Értékelés: {a.ertekeles}")
    print(f"6. feladat: {legkisebb_ertekeles().nev}")
    print(f"7. feladat: {jatekok_2014_ota()[0]}, {jatekok_2014_ota()[1]}")
    print(f"8. feladat: {tobb_mint_ket_jatek_egy_evben()[0]}, {tobb_mint_ket_jatek_egy_evben()[1]}, {tobb_mint_ket_jatek_egy_evben()[2]}")



def beolvas(fajlnev:str):
    file = open(fajlnev, "r", encoding="utf8")
    file.readline()
    for row in file:
        jatekok.append(Jatek(row))

def akcio_jatekok():
    list = []
    for j in jatekok:
        if j.mufaj == "akcio":
             list.append(j)
    return list

def legkisebb_ertekeles():
    min_ertekeles = 1000
    min_jatek = ""
    for j in jatekok:
        if j.ertekeles < min_ertekeles:
            min_ertekeles = j.ertekeles
            min_jatek = j
    return min_jatek

def jatekok_2014_ota():
    list = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    for j in jatekok:
        if j.datum in list:
            list.remove(j.datum)
    return list

def tobb_mint_ket_jatek_egy_evben():
    dict = {}
    list = []
    list2 = []
    for j in jatekok:
        if j.datum not in dict.keys():
            dict[j.datum] = 1
        else:
            dict[j.datum] += 1
    


    for key,value in dict.items():
        if value > 2:
            list.append(key)


    for j in jatekok:
        if j.datum in list:
            list2.append(j.nev)

    return list2
main()