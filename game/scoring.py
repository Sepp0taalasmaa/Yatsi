import scorecard

class Scoring:
	def __init__(self):
		pass

	def calcScore(self, scard:"scorecard.Scorecard", dice:list, input:str): #antaa ValueError jos antaa yhdistelmän jota ei voi käyttää
		hands = scard.validHands(dice) #[yhdistelmät, noppien määrät]
		if input in hands[0]:
			if "-" in input:
				input = input.split("-")
				if len(input) == 2:
					match input[1]:
						case "Pari":
							scard.scores["pair"] = int(input[0])*2
						case "Kolmoisluku":
							scard.scores["3oak"] = int(input[0])*3
						case "Neloisluku":
							scard.scores["4oak"] = int(input[0])*4
						case _:
							raise ValueError
				elif len(input) == 3:
					match input[2]:
						case "Kaksi paria":
							scard.scores["2pair"] = int(input[0])*2 + int(input[1])*2
						case "Täyskäsi":
							scard.scores["FullH"] = hands[1][int(input[0])-1]*int(input[0]) + hands[1][int(input[1])-1]*int(input[1])
						case _:
							raise ValueError
				else:
					raise ValueError
			else:
				match input:
					case "Yatzy":
						scard.scores["yatzy"] = 50
					case "Ykköset":
						scard.scores["1s"] = hands[1][0]*1
					case "Kakkoset":
						scard.scores["2s"] = hands[1][1]*2
					case "Kolmoset":
						scard.scores["3s"] = hands[1][2]*3
					case "Neloset":
						scard.scores["4s"] = hands[1][3]*4
					case "Viitoset":
						scard.scores["5s"] = hands[1][4]*5
					case "Kuutoset":
						scard.scores["6s"] = hands[1][5]*6
					case "Pieni suora":
						scard.scores["1-5"] = 15
					case "Suuri suora":
						scard.scores["2-6"] = 20
					case "Sattuma":
						scard.scores["misc"] = sum(dice)
					case _:
						raise ValueError
		else:
			raise ValueError

		if scard.scores["bonus"] == 0:
			if scard.vsumma >= 63:
				scard.scores["bonus"] = 50