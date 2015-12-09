from django.http import HttpResponse
from django.shortcuts import render
import json
from blockchain.wallet import Wallet
from blockchain import createwallet

def login(request):
	return HttpResponse('')

def signin(request):
	login=request.GET.get('login')
	password=request.GET.get('password')

	if login and password:
		#wallet = createwallet.create_wallet('password', 'API key', label = 'Test swallet')
		return HttpResponse('{status:"ok"}')
	return HttpResponse('{status:"login or password not input"}')

def get_balance(request):
	login=request.GET.get('login')
	password=request.GET.get('password')

	if login and password:
		wallet = Wallet(login, password)
		try:
			balance=wallet.get_balance()
		except BaseException:
			return HttpResponse('{"status":"API not allowed in yours account or login or password is uncorrected"}')
		return HttpResponse('{"status":"ok", "balance":'+ str(balance) +'}')
	return HttpResponse('{"status":"login or password not input"}')

def home(request):
	return render(request, 'index.html')