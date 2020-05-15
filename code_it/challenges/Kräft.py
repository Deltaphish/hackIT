import random
import base64
from itertools import cycle

class Festival1:
	def __init__(self):
		self.description	=	'''	
									It's time for the annual smurf year festival! However there is already a problem.
									Normaly at the feast a smurfberry scented candle is placed on the right to each smurfs plate.
									However some smurfs are complaining that they keep getting knocked down and should be placed on the left.
									Neutral smurf has convinced some that there should be a candle on both sides and the rest think the whole thing
									is stupid, and are now demanding that there should be no candles at all!

									Fearing a smurf revolt, pappa smurf annonces that everyone will get what they want. But due to a shortage of
									candles he knows he needs a clever solution.

									Your mission: Given a list of n smurfs with a prefrence R(ight),L(eft),B(oth), or N(one) find a placement on a round
									table so that every smurf gets his prefrence and no candles are wasted. Assume that there is exists an optimal solution.

									EX: LLLLLBBRRRRRN -> RLRLRLRLRBBLN
								'''

	def prompt (self,seed):
		random.seed(seed)
		candles = random.choices([True,False],cum_weights = ( 0.60 , 1.0 ),k=21)
		seatings = ""
		for i in range(len(candles)):
			if candles[i-1] and candles[i]:
				seatings += 'B'
			elif candles[i-1] and not candles[i]:
				seatings += 'L'
			elif not candles[i-1] and candles[i]:
				seatings += 'R'
			else:
				seatings += 'N'

		return ("".join(sorted(seatings)))

	def validate(self,ans,seed):
		q = self.prompt(seed)
		if sorted(ans) != sorted(q):
			return False
		if len(ans) != 21:
			return False
		if set(ans) != set('BLRN') :
			return False
		for i in range(len(ans)):
			current = ans[i-1]
			neigbour = ans[i]
			if current == 'B' and (neigbour == "R" or neigbour == "N"):
				return False
			elif current == 'L' and (neigbour == "L" or neigbour == "B"):
				return False
			elif current == 'R' and (neigbour == "R" or neigbour == "N"):
				return False
			elif current == 'N' and (neigbour == "L" or neigbour == "B"):
				return False
		return True

id = "festival"
title = "Smurfestival"

subchallenges = [
	Festival1(),
]
