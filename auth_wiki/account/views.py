from django.shortcuts import render, redirect
from.forms import NewUserForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('library:home')
        messages.error(request, "Unsuccessful registration. Invalid information.")    
            
    form = NewUserForm()
    context={
        'register_form':form,
    }
    return render(request,'account/register.html',context)

def userlogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("library:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
    
	return render(request, "account/login.html", context={"login_form":form})

def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("library:home")

@login_required
def profile(request):
    return render(request,"account/profile.html")   
fields=['user','first_name','last_name','gender','image','contact_number', 'created_on', 'updated_on']
def create_profile(request):
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
        
    return render(request,'account/createprofile.html')

# def seller_profile(request,id):
#     seller = User.objects.get(id=id)
#     context={
#         'seller':seller,
#     }
#     return render (request,'users/sellerprofile.html',context)