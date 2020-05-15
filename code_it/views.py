from django.shortcuts import render, redirect
from django.views.decorators.http  import require_POST
from .challenges import Crypto, Kräft


def genSeed(id):
	# Takes a string and generates integer smaller than 10^10.
	# Could probably just use hash(), but this is funner
	seed = ""
	for c in id:
		seed += str(ord(c))
	while len(seed) >= 10:
		size = len(seed)
		s1 = seed[0:int(size/2)]
		s2 = seed[int(size/2):]
		seed = str(int(s1) ^ int(s2))
	return int(seed)

class ChallengeHandler:
	def __init__(self):
		self.challenges = {
			"crypto" : Crypto,
			"festival": Kräft, 
		}
	def get(self,key):
		if key in self.challenges:
			return self.challenges[key]
		else:
			return None

def index(request):
	ch = ChallengeHandler()
	titles = map(lambda tp: dict(id = tp[0],title = tp[1].title), ch.challenges.items())
	context = {
		'challenge_list' : titles,
		'login':request.session.get('login')
	}
	return render(request, 'code_it/index.html',context)

def detail(request,id):
	ch = ChallengeHandler()
	username = request.session.get('login')
	if username:
		seed = genSeed(username)
		challenge = ch.challenges.get(id)
		if challenge:
			if not request.session.get(challenge.id + "-progress"):
				request.session[challenge.id + "-progress"] = 0
			
			current_challenge = request.session[challenge.id + "-progress"]
			if current_challenge >= len(challenge.subchallenges):
				return render(request, 'code_it/succsess.html',{
															"title" : challenge.title,
															"login" : request.session.get('login'),
															"id" 	: challenge.id,
															})
			return render(request,'code_it/details.html',{
															"id" : challenge.id,
															"title" : challenge.title,
															"current_challenge" : current_challenge,
															"challenges" : challenge.subchallenges[0:(current_challenge+1)],
															"prompt" : challenge.subchallenges[current_challenge].prompt(seed),
															"login" : request.session.get('login'),
														})
	else:
		return redirect("login")

def reset(request):
	id = request.GET['id']
	request.session[id+"-progress"] = 0
	return redirect("code_it")

@require_POST
def validate_answer(request):
	if username := request.session.get('login'):
		ch = ChallengeHandler()
		id = request.POST['challenge_id']
		level = request.POST['challenge_level']
		answer = request.POST['answer']
		if challenge := ch.get(id):
			if challenge.subchallenges[int(level)].validate(answer,genSeed(username)):
				request.session[id+"-progress"] += 1
			return redirect('/code/'+challenge.id)
			
