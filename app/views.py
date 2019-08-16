from django.shortcuts import render
from django.views import View

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from app.models import Post

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class PostList(View):
    template = 'post_list.html'
    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template, {'posts':posts})


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'resumo', 'imagem']
    success_url = reverse_lazy('main')


@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'resumo', 'imagem']


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')