from django import forms

from app.models import UsuarioModel, Blog, Categoria


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': True}
        )
    )

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()


    class Meta:
        model = UsuarioModel
        exclude = ('email', 'date_joined', 'is_staff', 'user_permissions', 'groups', 'is_active')


class PostForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['title', 'texto', 'image', 'categoria']


class CategoriaForm(forms.ModelForm):
    class Meta():
        model = Categoria
        fields = ['titulo', 'image']