from distutils.command.build_scripts import first_line_re
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
# Create your views here.

# def index(request):
#     # template = loader.get_template('myfirst.html')
#     # return HttpResponse(template.render())
#     mymembers = Members.objects.all().values()
#     output = []
#     for x in mymembers:
#         output.append(x['firstname'])
#     # return render(request, 'myfirst.html')
#     return HttpResponse(output)

def index(request):
    mymembers = Members.objects.all().values()
    # template = loader.get_template('index.html')
    # context = {
    #     'mymembers': mymembers,
    # }
    return render(request, 'index.html',{'mymembers': mymembers})

def add(request):
    return render(request,'add.html')

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()

    return HttpResponseRedirect(reverse('index'))



   