from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

def usersignup(request):
	context = {
	'form': 'UserSignupForm'
	}
	if request.method == 'POST':
		form = UserSignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			auth = authenticate(username=username, password=password)
			login(request, auth_user)

			return redirect("/")
		return redirect("cafe:signup")
	return render(request, 'signup.html', context)

def userlogin(request):
	context = {
	'form': 'UserLoginForm'
	}

	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			auth = authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				return redirect("/")
			return redirect("cafe:login")
		return redirect("cafe:login")
	return render(request, 'signup.html', context)



def userlogout(request):
	logout(request)
	return redirect ('cafe:login')
