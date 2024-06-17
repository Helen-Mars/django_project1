from django.db import models
from django.contrib.auth.models import User


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')  # 用于一般文件
    my_image = models.ImageField(upload_to='images/')  # 用于图片文件
    my_url = models.URLField()
    my_field = models.CharField(max_length=100)
    my_integer = models.IntegerField(default=0)
    my_date = models.DateField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username


