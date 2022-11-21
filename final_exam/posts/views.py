from django.views import generic
from django.shortcuts import render
from .models import Post
from .forms import ImageForm

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

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