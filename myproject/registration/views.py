from email import message
from django.shortcuts import render
from . import forms

# Create your views here.

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        message = 'You registed successfull. Thank you!'
    else:
        message = 'Input your information to register!'
    return render(request,'signup.html',{'message':message, 'form':form})