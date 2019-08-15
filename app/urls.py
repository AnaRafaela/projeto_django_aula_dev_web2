from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostCreate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('add/', PostCreate.as_view(), name='post-add'),
    #path('<int:pk>/', PostUpdate.as_view(), name='post-update'),
    #path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
