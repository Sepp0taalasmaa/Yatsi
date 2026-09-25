import random

pojot = 0
kirja = ["Ykköset", "Kakkoset", "Kolmoset",
         "Neloset", "Viitoset", "Kuutoset"]
nopat = [] 

for i in range(5):
    nopat.append(random.randint(1,6))
print(nopat)

for luku in range(1,7):
    pisteet = nopat.count(luku) * luku
    print(f"{kirja[luku -1]}: {pisteet}")

for luku in nopat:
    if luku == 1:
        pojot += 1
        print(pojot)
with open("pöytäkirja.txt", "w") as tiedosto:
    tiedosto.write(f"pelaaja1;{pojot}")