from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .forms import UsuarioForm, PostForm, CategoriaForm
from .models import UsuarioModel, Blog, Categoria


from django.contrib.auth import authenticate, login, logout
# Create your views here.

class IndexView(View):
    template = 'main.html'

    def get(self, request):
        model = Blog.objects.all()
        classes = Categoria.objects.all()
        paginator = Paginator(model, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, self.template, {'posts':posts, 'classes':classes})


@login_required
def visualizar_posts(request, id):
    model = Blog.objects.all().filter(categoria=id)
    cat = Categoria.objects.all().filter(id=id)
    paginator = Paginator(model, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'app/posts.html', {'posts': posts, 'cat':cat})


class CadastroUsuarioView(View):
    template = 'create_user.html'

    def get(self,request):
        form = UsuarioForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = UsuarioModel.objects.latest('id')
            usuario.save()
            return redirect('login_user')
        return render(request, self.template, {'form': form})

class LoginUserView(View):
    template = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('principal')
        return render(request, self.template)

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            return redirect('login_user')
        login(request, user)
        return redirect('principal')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_user')


class Administracao(View):
    template = 'adminstracao.html'

    def get(self, request):
        posts = Blog.objects.all()
        categorias = Categoria.objects.all()
        return render(request, self.template, {'posts':posts, 'categorias':categorias})

class Post(View):
    template = 'app/post_new.html'

    def get(self,request):
        form = PostForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('administracao')
        return render(request, self.template, {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Blog, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('administracao')
    return render(request, 'app/post_new.html', {'form':form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('administracao')
    return render(request, 'app/post_delete.html', {'form':post})


@login_required
def new_categoria(request):
    form = CategoriaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('administracao')
    return render(request, 'app/categ_new.html', {'form':form})

@login_required
def edit_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    form = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('administracao')
    return render(request, 'app/categ_new.html', {'form':form})


@login_required
def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('administracao')
    return render(request, 'app/categoria_delete.html', {'form':categoria})