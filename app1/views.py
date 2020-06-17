from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'a1.html',{'titles':'Dynamic'})
def about(request):
    return render(request,'a1.html',{'titles':'about','link':' http://127.0.0.1:8000/'})
def expression(request):
    a= int(request.POST['text1'])
    b= int(request.POST['text2'])
    c= a+b
    return render(request,'output.html',{'result':c})