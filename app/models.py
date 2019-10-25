from django.db import models
from django.contrib.auth.models import User


class UsuarioModel(User):

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='imagens', blank=True)

    def __str__(self):
        return self.titulo


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    texto = models.TextField()
    image = models.ImageField(upload_to='imagens', blank=True)
    created_at = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
