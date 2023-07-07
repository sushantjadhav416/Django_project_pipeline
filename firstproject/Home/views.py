from django.shortcuts import render , HttpResponse
from Home.models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is my about page!")

def Home(request):
    return render(request,'Home.html')

def contact(request):
    if request.method == "POST":
       Name = request.POST.get('name')
       Email = request.POST.get('email')
       Password = request.POST.get('password')
       Phone = request.POST.get('phone')
       Desc = request.POST.get('desc')
       contact = Contact(name=Name,email=Email,password=Password,phone=Phone,desc=Desc)
       contact.save()
    return render(request,'Contact.html')


