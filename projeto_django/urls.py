"""projeto_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='principal'),
    path('login_user/', views.LoginUserView.as_view(), name="login_user"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('cadastro/usuario/', views.CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('administracao/', views.Administracao.as_view(), name='administracao'),
    path('categoria/new/', views.new_categoria, name='categoria_new'),
    path('categoria/edit/<int:id>', views.edit_categoria, name='edit_categoria'),
    path('categoria/delete/<int:id>', views.delete_categoria, name='delete_categoria'),
    path('post/<int:id>', views.visualizar_posts, name='visualizar_posts'),
    path('post/new/', views.Post.as_view(), name='post_new'),
    path('post/delete/<int:id>', views.delete_post, name='delete_post'),
    path('post/edit/<int:id>', views.edit_post, name='edit_post'),
    path('blog/', include('app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
