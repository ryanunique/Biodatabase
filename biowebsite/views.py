from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .models import remark
from .models import ongoin
from .models import Students

def home(request):

	records=Record.objects.all()
	Remarks = remark.objects.all()
	Ongoing = ongoin.objects.all()
	Studentss = Students.objects.all()
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user= authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request, "You have Successfuly Logged in!")
			return redirect('home')
		else:
			messages.success(request,"Username OR password is incorrect")
			return redirect('home')
	else:
		
		return render(request, 'home.html', {'records': records, 'remarks': Remarks, 'Ongoing': Ongoing, 'Students': Studentss})

	
	

def login_user (request):
	# check if user is loging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user= authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request, "You have Successfuly Logged in!")
			return redirect('home')
		else:
			messages.success(request,"Username OR password is incorrect")
			return redirect('home')
	else:
		return render (request,'home.html',{})


def logout_user(request):
	logout(request)
	messages.success(request,"You have been logout...")
	return redirect ('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username= username , password= password )
			login(request,user)
			messages.success(request,'You have Successfully registerd')
			return redirect('home')
	else :
		form = SignUpForm()
		return render (request,'register.html',{'form':form})
	return render(request, 'register.html', {'form':form})

def students(request):
	return render(request,'students.html')