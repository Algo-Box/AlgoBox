from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Users.forms import SignUpForm

def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db() #retrieve all the handles and extra info.
			user.profile.bio = form.cleaned_data.get('bio')
			user.profile.cc_handle = form.cleaned_data.get('cc_handle')
			user.profile.cf_handle = form.cleaned_data.get('cf_handle')
			user.profile.sp_handle = form.cleaned_data.get('sp_handle')
			user.profile.ac_handle = form.cleaned_data.get('ac_handle')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})