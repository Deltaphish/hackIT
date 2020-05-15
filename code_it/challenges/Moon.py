import random
import base64
from itertools import cycle

class Crypto1:
	def __init__(self):
		self.description	=	'''	Astro smurf has finaly convinced papa smurf to fund the S.M.R.F (Space Missions and Research Force).
									and has been given a simple mission: get to the moon.

									The command module already build, now we only need to build the rockets. To generate enough power to lift the rocket we need
									one rocket
								'''
		self._keywords = [
			"lemon",
			"custard",
			"coward",
			"lizard",
			"pinky",
			"kinky",
			"blueberry",
			"applepie",
			"delicous",
			"cabal",
			"secret",
			"hotsauce",
			"dangerous",
			"kingmaker",
			"dawnslayer",
			"conspiracy",
			"gargamel",
			"please",
			"friend",
		]

		self._codenames = [
			"feline",
			"kitten",
			"paws",
			"jellybeans",
			"small kahuna",
			"wiskers",
			"fluffy",
			"boopy",
			"toby",
			"mittens",
			"furryboots",
			"snuggles",
		]

	def prompt (self,seed):
		random.seed(seed)
		key = random.choice(self._keywords)
		codename = random.choice(self._codenames)
		message = f"the only one you can trust is me. from now i will give the codename: {codename}. await futher instructions. paranoid smurf"
		return self._vig_encrypt(key,message)

	def validate(self,ans,seed):
		random.seed(seed)
		key = random.choice(self._keywords)
		codename = random.choice(self._codenames)
		try:
			answeres = ans.strip("(").strip(")").split(",")
			if key == answeres[1] and codename == answeres[0]:
				return True
			else:
				return False 
		except:
			return False

	def _vig_encrypt(self,key,message):
		key_offsets = cycle(map(lambda c: ord(c) - 97, key))
		cipher_text = ""
		for c in message.lower():
			if not c.isalpha():
				cipher_text += c
			else:
				cipher_text += chr((((ord(c) - 97) + next(key_offsets)) % 26) + 97)
		return(cipher_text)

class Crypto2:
	def __init__(self):
		self.description	=	'''	You reply using your new codename that you have recived his message.

									After a few days of silence you recive a haphazardly cobbled together letter unmistakenly written by paranoid smurf.
									With some considerable effort, you manage to interpret message:

									IF YOU WERE ABLE TO DECRYPT IT THEN THE MOLE SMURFS ALREADY KNOW EVERYTHING.
									LITTLE DO *THEY* KNOW I SOLD EVERYTHING TO BUY A SMURF-PUTER.
									HAHAHAHAHAHHAHAHAHAHH HA

									TRY TO DECODE THIS YOU SUBTERRANEAN DOGS

									on the backside of the letter is this:
								'''
		self.messages = [
			"Its true, I'm a genius",
			"I am the greatest smurf alive",
			"Goodluck reading this loser",
			"Real mamals live on the surface",
			"No one has ever said moles are cool",
			"Don't trust papa smurf, he feeds you lies",
			"Don't trust the moles, but voles are cool",
			"I see through the lies of the smurfs",
			"HAHA you can't even read this. HA",
			"Dead smurfs tell no lies, unless you are zombie smurf",
		]

	def prompt(self,seed):
		random.seed(seed)
		message = random.choice(self.messages)
		return self._encrypt(message)

	def _encrypt(self,message):
		# Convert text to base64, then to string, then to binary
		b64 = base64.b64encode(message.encode()).decode(encoding='ascii')
		
		result = ""
		for c in b64:
			bin = format(ord(c),'b')
			bin = bin.rjust(8,'0')
			result += bin
		return result

	def validate(self,ans,seed):
		random.seed(seed)
		message = random.choice(self.messages)
		return ans == message

id = "crypto"
title = "CryptoSmurf"

subchallenges = [
	Crypto1(),
	Crypto2(),
]
