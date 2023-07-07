from django.shortcuts import render , HttpResponse,redirect
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def fashion(request):
    return render(request,'fashion')

def contact(request):
    if request.method == "POST":
       Name = request.POST.get('name')
       Email = request.POST.get('email')
       Password = request.POST.get('password')
       confirm_password = request.POST.get('password2')
       Phone = request.POST.get('phone')
    #    contact = Contact(name=Name,email=Email,password=Password,phone=Phone,desc=Desc)
    #    contact.save()
       if Password == confirm_password:
           if User.objects.filter(username=Name).exists():
               messages.info(request,"The email is exists!!!")
               return redirect(contact)
           else:
               user = User.objects.create_user(username=Name,email=Email,password=Password)
               
               user.set_password(Password)
               user.save()
               messages.success(request,"Your profile is registered")
               return redirect('login')
       else:
           messages.info(request,"The both passwords are not matching!!")

    return render(request,'Contact.html')


def electronics(request):
    return render(request,'electronics.html')

def signup(request):

    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username =  request.POST.get('name')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            return redirect('Home')
        else:
            messages.info(request, "Invalid email or password")
            return redirect("login")

    return render(request,'login.html')
