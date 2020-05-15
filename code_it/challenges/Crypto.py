import random
import base64
from itertools import cycle

class Crypto1:
	def __init__(self):
		self.description	=	'''	Paranoid smurf needs your help to find the lizard smurfs that control papa smurf.
									However the letter he sends you is encrypted and paranoid smurf dosn't trust you with the key...

									What you do know is that all of his message ends with "paranoid smurf" and that the key is
									probably only three letters. Also he said something about discovering "the indecipherable cipher"...

									Answer format: (codename,key)

									The letter's content reads:
								'''
		self._keywords = [
			"dad",
			"sad",
			"lad",
			"rad",
			"mad",
			"cad",
			"car",
			"bar",
			"lat",
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

									TRY TO DECODE THIS YOU 8 BIT SUBTERRANEAN DOGS, XOR CAN YOU?

									on the backside of the letter is this:
								'''
		self.messages = [
			"its true what they say , i am a genius",
			"i am the greatest smurf alive, your welcome",
			"real mamals live on the surface, like monkeys",
			"no one has ever said moles are cool, voles however",
			"don't trust papa smurf, he feeds you only lies",
			"i see through the lies of the smurfs, i dont fear the gargamel as you do",
			"haha, you cant read this you filthy mole smurfs, eat some worms",
			"dead smurfs tell no lies, unless you are zombie smurf",
		]

	def prompt(self,seed):
		random.seed(seed)
		message = random.choice(self.messages)
		random_byte = random.getrandbits(8)
		return self._encrypt(message,random_byte)

	def _encrypt(self,message,byte):
		# Convert text to base64, then to string, then to binary		
		cipher_text = []
		for c in message:
			cipher_text.append(ord(c) ^ byte)
		encoded = base64.b64encode(bytearray(cipher_text))
		return encoded

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
