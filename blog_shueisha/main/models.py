from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

"""En esta seccion se plantean todos los modelos de los registros que va a tener la base de"""

# Modelo para almacenar los usuarios creados, donde se incluyen todos los campos que debe tener ese Usuario
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


# Modelo para almacenar archivos de imagenes que se cargan dentro de la página
class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

# Modelo para almacenar los blogs registrados en la web
class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

# Campos necesarios para registrar un nuevo blog de algún anime o manga
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


# Modelo para almacenar las reviews registradas y las nuevas ingresadas por nuevos usuarios.
class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

# Campos que deben ser llenados para las reviews
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
