from django.contrib import admin
from .models import User  


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','id','public_id','username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)

