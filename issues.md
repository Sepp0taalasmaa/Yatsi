# Yazy – GitHub Issues

## Issue 1: Luo projektin perusrakenne

### Tavoite
Luodaan projektille yhteinen kansio- ja tiedostorakenne, jonka päälle muut ominaisuudet voidaan rakentaa.

### Tehtävät
- Luo projektin kansiorakenne:
  - `main.py`
  - `game/`
  - `scoring/`
  - `ui/`
  - `tests/`
- Luo tarvittavat Python-tiedostot moduuleille:
  - `game/game.py`
  - `game/dice.py`
  - `game/player.py`
  - `game/scorecard.py`
  - `scoring/scoring.py`
  - `ui/console_ui.py`
- Lisää tarvittavat `__init__.py`-tiedostot.
- Lisää projektille `.gitignore`.
- Lisää README-tiedostoon lyhyt kuvaus projektin rakenteesta.

### Hyväksymiskriteerit
- [ ] Projekti käynnistyy `main.py`-tiedostosta ilman virheitä.
- [ ] Kaikki sovitut kansiot ja tiedostot löytyvät.
- [ ] Pythonin välimuisti- ja virtuaaliympäristötiedostoja ei tallenneta GitHubiin.

### Riippuvuudet
Ei riippuvuuksia.

### Ehdotettu branch
`feature/project-structure`

---

## Issue 2: Suunnittele moduulien väliset rajapinnat

### Tavoite
Sovitaan ennen toteutusta, miten eri moduulit keskustelevat keskenään.

### Tehtävät
Määritelkää ainakin:

#### Dice
- Miten nopat luodaan?
- Miten nopat heitetään?
- Miten valitut nopat lukitaan?
- Miten nykyiset noppien arvot saadaan?

#### Scoring
- Missä muodossa nopat annetaan pistelaskulle?
- Miten kategorian pisteet palautetaan?

#### Scorecard
- Miten käytettävissä olevat kategoriat saadaan?
- Miten pisteet tallennetaan?
- Miten kokonaispisteet saadaan?

#### Game
- Miten vuoro aloitetaan?
- Miten heittojen määrä käsitellään?
- Milloin vuoro päättyy?

### Hyväksymiskriteerit
- [ ] Moduulien vastuut on kirjattu README-tiedostoon.
- [ ] Moduulien tarvitsemat tärkeimmät metodit tai funktiot on nimetty.
- [ ] Jokainen ryhmän jäsen ymmärtää, mitä hänen moduulinsa vastaanottaa ja palauttaa.

### Riippuvuudet
Issue 1.

### Ehdotettu branch
`docs/module-interfaces`

---

# Nopat

## Issue 3: Toteuta viiden nopan hallinta

### Tavoite
Pelissä on aina viisi kuusisivuista noppaa.

### Tehtävät
- Toteuta viiden nopan muodostaminen.
- Jokaisen nopan arvon tulee olla 1–6.
- Toteuta kaikkien noppien heittäminen.
- Toteuta nykyisten noppien arvojen palauttaminen.

### Esimerkkitilanne
Noppien arvot voisivat olla:

`[2, 6, 1, 6, 4]`

### Hyväksymiskriteerit
- [ ] Pelissä on viisi noppaa.
- [ ] Jokainen noppa saa arvon väliltä 1–6.
- [ ] Nopat voidaan heittää uudelleen.
- [ ] Noppien nykyiset arvot voidaan lukea.

### Riippuvuudet
Issue 1 ja Issue 2.

### Ehdotettu branch
`feature/dice`

---

## Issue 4: Toteuta noppien lukitseminen

### Tavoite
Pelaaja voi päättää, mitkä nopat säilytetään seuraavaan heittoon.

### Tehtävät
- Mahdollista yhden tai useamman nopan lukitseminen.
- Lukittua noppaa ei heitetä uudelleen.
- Lukitus voidaan tarvittaessa poistaa.
- Lukittujen ja vapaiden noppien tila voidaan tarkistaa.

### Hyväksymiskriteerit
- [ ] Pelaaja voi lukita haluamansa nopat.
- [ ] Vain lukitsemattomat nopat heitetään uudelleen.
- [ ] Lukitus voidaan vaihtaa heittojen välillä.

### Riippuvuudet
Issue 3.

### Ehdotettu branch
`feature/dice-locking`

---

# Pistelasku

## Issue 5: Toteuta yläosan pistelasku

### Tavoite
Pistelasku osaa laskea Yazy-pistetaulukon yläosan kategoriat.

### Toteutettavat kategoriat
- Ykköset
- Kakkoset
- Kolmoset
- Neloset
- Viitoset
- Kuutoset

### Esimerkki
Nopat:

`[6, 6, 3, 6, 2]`

Kuutoset:

`18 pistettä`

### Hyväksymiskriteerit
- [ ] Jokaisen kategorian pisteet voidaan laskea.
- [ ] Pistelasku toimii riippumatta noppien järjestyksestä.
- [ ] Pistelaskumoduuli ei tulosta mitään ruudulle.
- [ ] Pistelaskumoduuli ei kysy käyttäjältä syötteitä.

### Riippuvuudet
Issue 2.

### Ehdotettu branch
`feature/scoring-upper`

---

## Issue 6: Toteuta pari, kaksi paria, kolmoset ja neloset

### Tavoite
Toteutetaan seuraavat pistelaskukategoriat:

- Pari
- Kaksi paria
- Kolme samaa
- Neljä samaa

### Huomioitavaa
Sopikaa ryhmässä tarkasti, miten kategorioiden pisteet määräytyvät ennen toteutusta.

### Hyväksymiskriteerit
- [ ] Pari tunnistetaan oikein.
- [ ] Kaksi eri paria tunnistetaan oikein.
- [ ] Kolme samaa tunnistetaan oikein.
- [ ] Neljä samaa tunnistetaan oikein.
- [ ] Virheellisestä yhdistelmästä palautuu 0 pistettä.

### Riippuvuudet
Issue 2.

### Ehdotettu branch
`feature/scoring-combinations`

---

## Issue 7: Toteuta suorat

### Tavoite
Toteutetaan pienen ja suuren suoran tunnistaminen.

### Pieni suora
`1, 2, 3, 4, 5`

### Suuri suora
`2, 3, 4, 5, 6`

### Hyväksymiskriteerit
- [ ] Pieni suora tunnistetaan.
- [ ] Suuri suora tunnistetaan.
- [ ] Noppien järjestys ei vaikuta tunnistamiseen.
- [ ] Väärä yhdistelmä antaa 0 pistettä.

### Riippuvuudet
Issue 2.

### Ehdotettu branch
`feature/scoring-straights`

---

## Issue 8: Toteuta täyskäsi, sattuma ja Yazy

### Tavoite
Toteutetaan loput tärkeät pistelaskukategoriat.

### Kategoriat
- Täyskäsi
- Sattuma
- Yazy

### Hyväksymiskriteerit
- [ ] Täyskäsi tunnistetaan.
- [ ] Sattuma laskee noppien yhteispisteet.
- [ ] Viisi samaa tunnistetaan Yazyksi.
- [ ] Virheelliset yhdistelmät käsitellään oikein.

### Riippuvuudet
Issue 2.

### Ehdotettu branch
`feature/scoring-final`

---

# Pistetaulukko

## Issue 9: Toteuta pelaajan pistetaulukko

### Tavoite
Pelaajalla on oma pistetaulukko, johon eri kategorioiden pisteet tallennetaan.

### Tehtävät
- Luo kaikki käytettävät pistekategoriat.
- Merkitse aluksi kategoriat käyttämättömiksi.
- Mahdollista pisteiden tallentaminen kategoriaan.
- Sama kategoria voidaan käyttää vain kerran.
- Toteuta käytettävissä olevien kategorioiden hakeminen.

### Hyväksymiskriteerit
- [ ] Kaikki kategoriat löytyvät pistetaulukosta.
- [ ] Käyttämättömät kategoriat voidaan tunnistaa.
- [ ] Piste voidaan tallentaa kategoriaan.
- [ ] Käytettyä kategoriaa ei voi käyttää uudelleen.

### Riippuvuudet
Issue 2.

### Ehdotettu branch
`feature/scorecard`

---

## Issue 10: Toteuta pistetaulukon summat ja bonus

### Tavoite
Pistetaulukko osaa laskea pelaajan kokonaispisteet.

### Tehtävät
- Laske yläosan pisteiden summa.
- Toteuta Yazy-sääntöjen mukainen bonus.
- Laske kaikkien kategorioiden yhteispisteet.
- Toteuta tarkistus, onko pistetaulukko valmis.

### Hyväksymiskriteerit
- [ ] Yläosan summa lasketaan oikein.
- [ ] Bonus lisätään oikeassa tilanteessa.
- [ ] Kokonaispistemäärä voidaan hakea.
- [ ] Pistetaulukosta voidaan tarkistaa, onko peli pelaajan osalta valmis.

### Riippuvuudet
Issue 9.

### Ehdotettu branch
`feature/scorecard-totals`

---

# Pelaaja

## Issue 11: Toteuta pelaaja

### Tavoite
Jokaisella pelaajalla on nimi ja oma pistetaulukko.

### Tehtävät
- Luo pelaajalle nimi.
- Luo pelaajalle oma pistetaulukko.
- Mahdollista pelaajan pisteiden hakeminen.

### Hyväksymiskriteerit
- [ ] Pelaajalla on nimi.
- [ ] Jokaisella pelaajalla on oma erillinen pistetaulukko.
- [ ] Pelaajan kokonaispisteet voidaan tarkistaa.

### Riippuvuudet
Issue 9.

### Ehdotettu branch
`feature/player`

---

# Pelilogiikka

## Issue 12: Toteuta yhden pelaajan vuoro

### Tavoite
Pelaaja pystyy pelaamaan yhden kokonaisen Yazy-vuoron.

### Vuoron kulku

1. Ensimmäinen heitto.
2. Pelaaja valitsee säilytettävät nopat.
3. Toinen heitto.
4. Pelaaja voi muuttaa säilytettäviä noppia.
5. Kolmas heitto.
6. Pelaaja valitsee pistekategorian.
7. Pisteet tallennetaan.

### Hyväksymiskriteerit
- [ ] Vuorossa on enintään kolme heittoa.
- [ ] Noppia voidaan lukita heittojen välillä.
- [ ] Vuoron lopuksi valitaan pistekategoria.
- [ ] Pisteet tallentuvat pelaajan pistetaulukkoon.
- [ ] Vuoro päättyy pisteiden tallentamiseen.

### Riippuvuudet
Issue 4, Issue 5–8, Issue 9 ja Issue 11.

### Ehdotettu branch
`feature/player-turn`

---

## Issue 13: Toteuta usean pelaajan peli

### Tavoite
Pelissä voi olla vähintään kaksi pelaajaa.

### Tehtävät
- Luo pelin alussa pelaajat.
- Vaihda vuoro pelaajalta toiselle.
- Huolehdi, että jokaisella pelaajalla on oma pistetaulukko.
- Jatka peliä, kunnes kaikkien pistetaulukot ovat täynnä.

### Hyväksymiskriteerit
- [ ] Pelissä voidaan käyttää vähintään kahta pelaajaa.
- [ ] Vuoro vaihtuu oikein.
- [ ] Pelaajien pisteet eivät sekoitu keskenään.
- [ ] Peli tunnistaa, milloin kaikki kierrokset on pelattu.

### Riippuvuudet
Issue 11 ja Issue 12.

### Ehdotettu branch
`feature/multiplayer`

---

## Issue 14: Toteuta pelin päättyminen ja voittajan määrittäminen

### Tavoite
Kun kaikki kategoriat on käytetty, peli päättyy ja tulokset lasketaan.

### Tehtävät
- Tarkista kaikkien pistetaulukkojen valmistuminen.
- Laske pelaajien kokonaispisteet.
- Selvitä suurimman pistemäärän saanut pelaaja.
- Huomioi mahdollinen tasapeli.

### Hyväksymiskriteerit
- [ ] Peli päättyy oikeassa vaiheessa.
- [ ] Kaikkien pelaajien loppupisteet lasketaan.
- [ ] Voittaja voidaan määrittää.
- [ ] Tasapeli ei aiheuta virhettä.

### Riippuvuudet
Issue 10 ja Issue 13.

### Ehdotettu branch
`feature/game-ending`

---

# Käyttöliittymä

## Issue 15: Toteuta komentorivikäyttöliittymän perustoiminnot

### Tavoite
Pelaaja pystyy käyttämään peliä komentoriviltä.

### Käyttöliittymän tulee näyttää
- pelaajan nimi
- nykyinen vuoro
- heiton numero
- noppien arvot
- lukitut nopat
- käytettävissä olevat pistekategoriat
- pistetaulukko

### Käyttöliittymän tulee kysyä
- mitkä nopat säilytetään
- halutaanko heittää uudelleen
- mihin kategoriaan pisteet tallennetaan

### Hyväksymiskriteerit
- [ ] Pelaaja näkee noppien arvot.
- [ ] Pelaaja pystyy valitsemaan säilytettävät nopat.
- [ ] Pelaaja pystyy valitsemaan pistekategorian.
- [ ] Pistetaulukko voidaan näyttää.
- [ ] Käyttöliittymä ei itse laske pisteitä.

### Riippuvuudet
Issue 12.

### Ehdotettu branch
`feature/console-ui`

---

## Issue 16: Lisää käyttäjän syötteiden tarkistus

### Tavoite
Virheelliset syötteet eivät saa kaataa peliä.

### Tarkistettavia tilanteita
- käyttäjä antaa tekstin, vaikka odotetaan numeroa
- käyttäjä valitsee nopan, jota ei ole olemassa
- käyttäjä valitsee saman nopan monta kertaa
- käyttäjä valitsee jo käytetyn pistekategorian
- käyttäjä antaa tyhjän syötteen väärässä tilanteessa

### Hyväksymiskriteerit
- [ ] Virheellinen syöte ei kaada ohjelmaa.
- [ ] Käyttäjä saa ymmärrettävän virheilmoituksen.
- [ ] Virheen jälkeen käyttäjä voi yrittää uudelleen.

### Riippuvuudet
Issue 15.

### Ehdotettu branch
`feature/input-validation`

---

# Testaus

## Issue 17: Tee testit pistelaskulle

### Tavoite
Pistelaskun toimivuus varmistetaan automaattisilla testeillä.

### Testaa ainakin
- ykköset–kuutoset
- pari
- kaksi paria
- kolme samaa
- neljä samaa
- pieni suora
- suuri suora
- täyskäsi
- sattuma
- Yazy

### Mukaan tulee ottaa
- onnistuvia tapauksia
- epäonnistuvia tapauksia
- erilaisia noppien järjestyksiä

### Hyväksymiskriteerit
- [ ] Jokaiselle pistekategorialle on testejä.
- [ ] Testit voidaan ajaa yhdellä komennolla.
- [ ] Kaikki testit menevät läpi.

### Riippuvuudet
Issue 5–8.

### Ehdotettu branch
`test/scoring`

---

## Issue 18: Tee testit pistetaulukolle ja nopille

### Tavoite
Testataan pelin keskeiset tietorakenteet.

### Testaa nopista
- noppia on viisi
- arvot ovat välillä 1–6
- lukittu noppa ei vaihdu heitettäessä
- vapaa noppa voidaan heittää uudelleen

### Testaa pistetaulukosta
- pisteen tallentaminen
- saman kategorian käyttäminen kahdesti estetään
- summien laskeminen
- bonus
- pistetaulukon valmistuminen

### Hyväksymiskriteerit
- [ ] Noppien keskeiset toiminnot on testattu.
- [ ] Pistetaulukon keskeiset toiminnot on testattu.
- [ ] Testit menevät läpi.

### Riippuvuudet
Issue 4 ja Issue 10.

### Ehdotettu branch
`test/game-components`

---

# Viimeistely

## Issue 19: Viimeistele README

### Tavoite
Projektin GitHub-sivulta selviää, mikä projekti on ja miten sitä käytetään.

### README:n tulee sisältää
- projektin kuvaus
- Yazy-pelin lyhyt kuvaus
- käytetyt teknologiat
- projektin kansiorakenne
- asennusohje
- käynnistysohje
- testien ajo-ohje
- ryhmän jäsenet
- moduulien vastuut

### Hyväksymiskriteerit
- [ ] Uusi käyttäjä pystyy asentamaan projektin README:n avulla.
- [ ] Uusi käyttäjä pystyy käynnistämään pelin.
- [ ] Projektin rakenne on dokumentoitu.

### Riippuvuudet
Kaikki tärkeimmät ominaisuudet valmiina.

### Ehdotettu branch
`docs/readme`

---

## Issue 20: Pelin integraatiotestaus ja viimeistely

### Tavoite
Varmistetaan, että kaikki ryhmän toteuttamat osat toimivat yhdessä.

### Testattavat asiat
- pelin käynnistäminen
- pelaajien luominen
- ensimmäinen heitto
- noppien lukitseminen
- uudelleen heittäminen
- pistekategorian valinta
- pisteiden tallentuminen
- vuoron vaihtuminen
- koko pelin pelaaminen loppuun
- voittajan näyttäminen

### Lisäksi
- poistetaan tarpeettomat debug-tulostukset
- tarkistetaan muuttujien ja funktioiden nimet
- tarkistetaan koodin luettavuus
- tarkistetaan, ettei samaa logiikkaa ole kopioitu useaan paikkaan

### Hyväksymiskriteerit
- [ ] Kokonainen peli voidaan pelata alusta loppuun.
- [ ] Ohjelma ei normaalissa käytössä kaadu.
- [ ] Eri moduulit toimivat yhdessä.
- [ ] Kaikki automaattiset testit menevät läpi.

### Riippuvuudet
Kaikki toiminnalliset issuet.

### Ehdotettu branch
`chore/final-integration`

