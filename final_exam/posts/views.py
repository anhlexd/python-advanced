from django.views import generic
# from django.shortcuts import render
from .models import Post
from .forms import ImageForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index2.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def image_upload_view(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                img_obj = form.instance
                return render(request, 'post_detail.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
        return render(request, 'post_detail.html', {'form': form})

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'index.html', param)
    else:
        return redirect('login') 

def signup(request):
    if request.method =='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            messages.info(request, 'Please enter valid Username or Password.')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
