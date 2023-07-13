from django.shortcuts import render



# Create your views here.
def index(request):
      return render(request, 'ARES/index.html')

def about(request):
      return render(request, 'ARES/about.html')
  
def booking(request):
      return render(request, 'ARES/booking.html')
  
def contact(request):
      return render(request, 'ARES/contact.html')
  
def menu(request):
      return render(request, 'ARES/menu.html')
  
def service(request):
      return render(request, 'ARES/service.html')
  
def team(request):
      return render(request, 'ARES/team.html')
  
def register(request):
      return render(request, 'ARES/register.html')

def testimonial(request):
      return render(request, 'ARES/testimonial.html')
from django.shortcuts import render,redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 







def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('ARES:login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('ARES:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('ARES:login')
