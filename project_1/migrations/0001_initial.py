# Generated by Django 5.0 on 2024-06-14 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='files/')),
                ('my_image', models.ImageField(upload_to='images/')),
                ('my_url', models.URLField()),
                ('my_field', models.CharField(max_length=100)),
                ('my_integer', models.IntegerField(default=0)),
                ('my_date', models.DateField()),
            ],
        ),
    ]
