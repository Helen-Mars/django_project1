from django.db import models


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')  # 用于一般文件
    my_image = models.ImageField(upload_to='images/')  # 用于图片文件
    my_url = models.URLField()
    my_field = models.CharField(max_length=100)
    my_integer = models.IntegerField(default=0)
    my_date = models.DateField()


