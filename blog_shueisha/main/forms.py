from django import forms
from .models import Blog

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""En Esta seccion se colocan todos los formularios que son utilizados para obtener información ingresada por el usuario"""


# Formulario para que el usuario pueda ingresar una nueva review de algún anime o manga
class ReviewForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,			# Campo para el author de la review del anime
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True,			# Campo para el Nombre del anime
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True,	# Campo para la descripcion
		widget=forms.TextInput(attrs={
			'placeholder': '*Description info..',
			}))
	body = forms.CharField(max_length=500, required=True,			# Campo para el contenido de la review
		widget=forms.Textarea(attrs={
			'placeholder': '*Body info..',
			}))
	image = forms.ImageField()										# Campo para subir una imagen del anime

	class Meta:
		model = Blog
		fields = ['author', 'name', 'description', 'body', 'image']

# Formulario para ingresar un nuevo blog de anime o manga
class BlogForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,  
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Description info..',
			}))
	body = forms.CharField(max_length=500, required=True,
		widget=forms.Textarea(attrs={
			'placeholder': '*Body info..',
			}))
	image = forms.ImageField()

	class Meta:
		model = Blog
		fields = ['author', 'name', 'description', 'body', 'image']

# Formulario para crear un nuevo usuario en el sistema
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']