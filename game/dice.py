from random import randint

class Dice:
	def __init__(self):
		self.vals = [0,0,0,0,0] #noppien arvot voi saada suoraan .vals listasta

	def roll(self, d="11111"): #"d" valitsee mitkä nopat heitetään esim "01011" heittää noppia 2, 4 ja 5
		if len(d) != 5:
			raise ValueError
		else:
			for i in range(5):
				if d[i] == "1":
					self.vals[i] = randint(1,6)
				elif d[i] == "0":
					pass
				else:
					raise ValueError