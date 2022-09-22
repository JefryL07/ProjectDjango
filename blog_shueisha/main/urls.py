from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

"""En esta sección se encuenyran las urls de acceso a las páginas para lograr visialuzar el contenido de la web"""

app_name = "main"

urlpatterns = [
# Sección principales para la vista de blos y reviews creadas
	path('', views.IndexView.as_view(), name="home"),
	path('blogs/', views.PortfolioView.as_view(), name="blogs"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('reviews/', views.BlogView.as_view(), name="reviews"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),

# Sección para la cuenta de usuario, Login, Register, Logout
	path('register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name= "login"),
	path('logout/', views.logoutUser, name="logout"),

# Sección para las principales partes para crear nuevos blos o reviews pero con restricciones de usuario para lograr crear
	path('blogaddinfo/', login_required(views.BlogAddInfo.as_view()), name='blogaddinfo'),
	path('reviewaddinfo/', login_required(views.ReviewAddInfo.as_view()), name='reviewaddinfo'),
	
	]

    