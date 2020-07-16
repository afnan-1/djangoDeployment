from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactus(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pic',blank=True)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
    