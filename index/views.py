from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Topic

import os, base64, requests

def index(request):
    topic_list = Topic.objects.order_by('id')[:5]
    context = {'topic_list' : topic_list,'login':request.session.get('login')}
    return render(request, 'index/index.html',context)

def about(request):
    context = {'login':request.session.get('login')}
    return render(request, 'index/about.html',context)

def loginView(request):
    request.session['github_state'] = base64.b64encode(os.urandom(16)).decode('utf-8').strip('=')
    context = {'client_id':os.environ.get('CLIENT_ID'),'state':request.session['github_state']}
    return render(request,'index/login.html',context)

def logout(request):
    request.session['login'] = None
    return redirect('index')

def Oauth(request):
    if 'state' in request.GET:
        if 'github_state' in request.session:
            code = request.GET['code']
            params = {'client_id':os.environ.get('CLIENT_ID'),'client_secret':os.environ.get('CLIENT_SECRET'),'code':code,'state':request.session['github_state']}
            headers = {'Accept':'application/json'}
            accsess_token = requests.post("https://github.com/login/oauth/access_token",params=params,headers=headers)
            request.session['github_access_token'] = accsess_token.json()['access_token']
            
            github_info = requests.get("https://api.github.com/user",headers={'Authorization': "token "+request.session['github_access_token']})
            request.session['login'] = github_info.json()['login']
            return redirect('index')
        else:
            return HttpResponse('Please login from the login page',status=401)
    else:
        return HttpResponse('Please login from the login page',status=401)


