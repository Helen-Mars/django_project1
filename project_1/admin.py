from django.contrib import admin
from .models import MyModel


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'phone_number', 'address')
#     # search_fields = ('username', 'email', 'phone_number', 'address')
#     # filter_horizontal = ('groups', 'user_permissions')
#
# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(MyModel)
