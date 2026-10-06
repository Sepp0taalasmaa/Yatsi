class Scorecard:
	def __init__(self):
		self.scores = {
			"1s":None,
			"2s":None,
			"3s":None,
			"4s":None,
			"5s":None,
			"6s":None,
			"bonus":None,
			"pair":None,
			"2pair":None,
			"3oak":None,
			"4oak":None,
			"1-5":None,
			"2-6":None,
			"FullH":None,
			"misc":None,
			"yatzy":None
		} #pistemäärät kaikista yhdistelmistä

	def validHands(self, dice:list) -> list:
		r = []

		n = [0,0,0,0,0,0] #numeroiden 1-6 määrät nopissa

		for x in dice:
			n[x-1] += 1

		if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
			if self.scores["yatzy"] == None:
				r.append("Yatzy")

		if 1 in dice:
			if self.scores["1s"] == None:
				r.append("Ykköset")

		if 2 in dice:
			if self.scores["2s"] == None:
				r.append("Kakkoset")

		if 3 in dice:
			if self.scores["3s"] == None:
				r.append("Kolmoset")

		if 4 in dice:
			if self.scores["4s"] == None:
				r.append("Neloset")

		if 5 in dice:
			if self.scores["5s"] == None:
				r.append("Viitoset")

		if 6 in dice:
			if self.scores["6s"] == None:
				r.append("Kuutoset")

		if n == [1,1,1,1,1,0]:
			if self.scores["1-5"] == None:
				r.append("Pieni suora")

		if n == [0,1,1,1,1,1]:
			if self.scores["2-6"] == None:
				r.append("Suuri suora")

		pairs = []
			
		for i in range(6):
			if n[i] >= 2:
				pairs.append(str(i+1))
				if self.scores["pair"] == None:
					r.append(str(i+1)+"-Pari")

		if len(pairs) == 2:
			if self.scores["2pair"] == None:
				r.append('-'.join(pairs)+"-Kaksi paria")

		
		for i in range(6):
			if n[i] >= 3:
				if self.scores["3oak"] == None:
					r.append(str(i+1)+"-Kolmoisluku")

				if len(pairs) == 2:
					if self.scores["FullH"] == None:
						r.append('-'.join(pairs)+"-Täyskäsi")


		if self.scores["4oak"] == None:
			for i in range(6):
				if n[i] >= 4:
					r.append(str(i+1)+"-Neloisluku")

		if self.scores["misc"] == None:
			r.append("Sattuma")

		return [r, n] #yhdistelmät [0] ja noppien määrät [1]

	@property
	def summa(self) -> int:
		r = 0
		for x, y in self.scores.items():
			try:
				r += y
			except TypeError:
				pass
		return r

	@property
	def vsumma(self) -> int:
		r = 0
		for i in range(6):
			try:
				r += self.scores[f"{i+1}s"]
			except TypeError:
				pass
		return r

	def printScores(self) -> None:
		print("Ykköset:", self.scores["1s"])
		print("Kakkoset:", self.scores["2s"])
		print("Kolmoset:", self.scores["3s"])
		print("Neloset:", self.scores["4s"])
		print("Viitoset:", self.scores["5s"])
		print("Kuutoset:", self.scores["6s"])

		print("Välisumma:", self.vsumma)
		print("Bonus:", bool(self.scores["bonus"]))
		
		print("Pari:", self.scores["pair"])
		print("Kaksi paria:", self.scores["2pair"])
		print("Kolmoisluku:", self.scores["3oak"])
		print("Neloisluku:", self.scores["4oak"])
		print("Pieni suora:", self.scores["1-5"])
		print("Suuri suora:", self.scores["2-6"])
		print("Täyskäsi:", self.scores["FullH"])
		print("Sattuma:", self.scores["misc"])
		print("Yatzy:", self.scores["yatzy"])

		print("Summa:", self.summa)