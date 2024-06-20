from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # 自定义字段
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # groups 和 user_permissions 关系字段直接定义在类中
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
    )

    class Meta:
        # 模型元数据设置
        db_table = 'tb_users'
        verbose_name = 'custom user'
        verbose_name_plural = 'custom users'
        ordering = ['username']

    def __str__(self):
        return self.username


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')  # 用于一般文件
    my_image = models.ImageField(upload_to='images/')  # 用于图片文件
    my_url = models.URLField()
    my_field = models.CharField(max_length=100)
    my_integer = models.IntegerField(default=0)
    my_date = models.DateField()
