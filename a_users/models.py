from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from environ import Env
env = Env()
Env.read_env()

ENVIRONMENT = env('ENVIRONMENT', default='production')
if ENVIRONMENT == 'production':
    from cloudinary.models import CloudinaryField

 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    if ENVIRONMENT == 'production':
        image = CloudinaryField(null=True, blank=True)
    else:
        image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar_default.svg')
        return avatar
    
    @property
    def name(self):
        if self.realname:
            name = self.realname
        else:
            name = self.user.username 
        return name
    
    
   