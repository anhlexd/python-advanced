# from django.shortcuts import render
# from django.db import models

# # Create your views here.
# from django.http import HttpResponse
# from .forms import UploadFileForm

# def fileUploaderView(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             upload(request.FILES['file'])
#             return HttpResponse("<h2> File uploaded successful !</h2>")
#         else:
#             return HttpResponse("<h2> File uploaded not successful !</h2>")
            
#     form = UploadFileForm()
#     return render(request, 'fileUploader.html',{'form':form})

# def upload(f):
#     file = open(f.name, 'wb+')
#     for chunk in f.chunks():
#         file.write(chunk)

from django.shortcuts import render
from .models import Animal, AnimalForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        f = AnimalForm(request.POST)
        if f.is_valid():
            f.save()
            # upload(request.POST)
            return HttpResponse("<h2> Save successfuly ! </h2>")
        else:
            return HttpResponse("<h2> Save not successfuly ! !</h2>")

    form = AnimalForm()
    return render(request, 'UpFile.html',{'form':form})