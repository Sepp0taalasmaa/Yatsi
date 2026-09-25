import random

#pelaajien_maara = int(input("Monta pelaajaa: "))
#print(pelaajien_maara)
kirja = ["Ykköset", "Kakkoset", "Kolmoset",
         "Neloset", "Viitoset", "Kuutoset"]
nopat = [] 

for i in range(5):
    nopat.append(random.randint(1,6))
print(nopat)

for luku in range(1,7):
    pisteet = nopat.count(luku) * luku
    print(f"{kirja[luku -1]}: {pisteet}")

