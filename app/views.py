from django.shortcuts import render
from django.views import View

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from app.models import Post

class PostList(View):
    template = 'post_list.html'
    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template, {'posts':posts})

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'resumo', 'imagem']
    success_url = reverse_lazy('main')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'resumo', 'imagem']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')