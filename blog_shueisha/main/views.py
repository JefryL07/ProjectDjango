from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
	)

from django.views import generic
from . forms import CreateUserForm, BlogForm, ReviewForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

"""En esta sección se encuentran las partes de las vistas y metodos para la correcta visualización de la web"""

# Función para lograr que un usuario se registre en el sistema 
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('main>login')

		context = {'form':form}
		return render(request, 'main/register.html', context)

# Función para lograr ingresar dentro del sistema, validando los credenciales
def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username Or password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)


# Función para cerrar la cesión 
def logoutUser(request):
	logout(request)
	return redirect('main:login')

# Vista para crear nuevos blogs en el sitio
class BlogAddInfo(generic.FormView):
	template_name = "main/blogaddinfo.html"
	form_class = ReviewForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you for contribute with the page :)')
		return super().form_valid(form)

# Vista para crear nuevas reviews para la página
class ReviewAddInfo(generic.FormView):
	template_name = "main/blogaddinfo.html"
	form_class = ReviewForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you for contribute with the page :)')
		return super().form_valid(form)

# Vista principal o menú de home donde se muestra el contenido principal de la web
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)

		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context

# Vista de portafolio donde se observan todos los blogs creados
class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

# Vista para ver los detalles de un blog
class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

# Vista para ver las reviews creadas 
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

# Vista para ver los detalles de una review
class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

