from multiprocessing import context
from django.contrib.auth.models import User

# Función para obtener la conexión con el usuario y tener acceso a todos los detalles que contiene
def project_context(request):

    context = {
        'me': User.objects.first(),
    }

    return context