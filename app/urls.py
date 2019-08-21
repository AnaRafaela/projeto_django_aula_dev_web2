from django.contrib import admin
from django.urls import path, include
from app.views import imagemView
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('imagem/{% user.username %}/', views.imagemView, name='imagem')
    #path('<int:pk>/', PostUpdate.as_view(), name='post-update'),
    #path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
