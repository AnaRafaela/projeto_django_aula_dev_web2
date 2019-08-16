from django.shortcuts import render, redirect
from django.views import View
from .models import UsuarioModel
from .forms import UsuarioForm

from django.core.paginator import Paginator
from app.models import Post

from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Main(View):
    template = 'main.html'
    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        lista_posts = paginator.get_page(page)
        return render(request, self.template, {'lista_posts':lista_posts})

class UsuarioView(View):
    template = 'create_user.html'
    
    def get(self,request):
        form = UsuarioForm()
        return render(request, self.template, {'form': form})
        
    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = UsuarioModel.objects.latest('id')
            usuario.groups.add(Group.objects.get(pk=1))
            usuario.save()
            return redirect('main')
            return render(request, self.template, {'form': form})

class LoginView(View):
    template = 'login.html'
    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            return redirect('login')
        login(request, user)
        return redirect('main')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')

