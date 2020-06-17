from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    if request.method == "POST":
        Username =request.POST['username']
        Firstname = request.POST['first_name']
        Lastname =request.POST['last_name']
        Email = request.POST['email_id']
        Password = request.POST['password']



        x=User.objects.create_user( username=Username,first_name=Firstname,last_name=Lastname,email=Email,password=Password)
        x.save()
        print("User created")
        return redirect('/')


    else :
        return render(request,'form.html')

