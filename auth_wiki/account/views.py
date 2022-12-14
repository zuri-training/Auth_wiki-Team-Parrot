from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def register(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method=='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
            # login(request, user)
			return redirect('account:login')

		return HttpResponse("Unsuccessful registration. Invalid information.")
            
	form = NewUserForm()
	context={
		'register_form':form,
	}
	return render(request,'signup.html', context)

def userlogin(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as {username}.")
				return redirect("/")
                
			else:
				return render(request, "login.html", context={"login_form":form, 'status':'error', 'alert_msg': 'User was not found try registering'})
				
		else:
			return render(request, "login.html", context={"login_form":form, 'status':'error', 'alert_msg': 'The form was invalid'})

	form = AuthenticationForm()
    
	return render(request, "login.html", context={"login_form":form})

def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect('account:login')
	# forms = AuthenticationForm()
	# return render(request, "login.html", context={"login_form":forms, 'status':'success', 'alert_msg': 'You have successfully logged out'})
 
	# return redirect("library")

@login_required(login_url='account:register')
def profile(request):
    return render(request, "profile.html")   


@login_required(login_url='account:register')
def Editprofile(request):
	if request.method=='POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		gender = request.POST.get('gender')
		contact_number = request.POST.get('contact_number')
        #created_on = request.POST.get('created_on')
        #updated_on = request.POST.get('updated_on')
		image = request.FILES['upload']
		user = request.user
		profile = Profile(user=user, image=image, contact_number=contact_number,first_name=first_name, last_name=last_name, gender=gender)
        #created_on=created_on, updated_on=updated_on)
		profile.save()
		return redirect("account:profile")
        
	return render(request,'create_profile.html')

@login_required(login_url='account:register')
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "account/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="setpassword.html", context={"password_reset_form":password_reset_form})