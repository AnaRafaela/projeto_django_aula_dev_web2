from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from app.models import Post
from app.forms import PostForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@login_required
def imagemView(request, id):
    imagem = get_object_or_404(Post, pk=id)
    return render(request, 'app/image.html', {'imagem': imagem} )


@method_decorator(login_required, name='dispatch')
class Perfil(View):
    template = 'perfil.html'
    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template, {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = request.user
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'app/post_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'resumo', 'imagem']


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
   