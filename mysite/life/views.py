from django.shortcuts import render
from django.http import HttpResponse
from .dbms import account
# Create your views here.


def life(request):
	return render(request,'life/life.html')

def about(request):
	return render(request,'life/about.html')

def contact(request):
	return render(request,'life/contact.html')

def login(request):
	return render(request,'life/login.html')

def search(request):
	return render(request,'life/search.html')

def sign(request):
	return render(request,'life/sign.html')

def get_in(request):
	data = {}
	if request.method == 'POST':
		data['phone'] = request.POST.get('phone')
		data['password'] = request.POST.get('password')
	
	if account.log_in(data):
		return render(request,'life/after.html',data)
	else:
		return HttpResponse("<h1>Log in failed</h1><p>Check username and password</p>")

def create_acc(request):
	data = {}
	if request.method == 'POST':
		data['name'] = request.POST.get('name')
		data['city'] = request.POST.get('city')
		data['email'] = request.POST.get('email')
		data['phone'] = request.POST.get('mobile')
		data['bloodgroup'] = request.POST.get('group1')
		data['password'] = request.POST.get('password')
	
	if account.create(data):
		return render(request,'life/dashboard.html',data)
	else:
		return HttpResponse("<h1>signup failed</h1>")