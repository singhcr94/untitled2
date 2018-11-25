from django.contrib import admin

# Register your models here.
from .models import person,customuser
admin.site.register(person)
#admin.site.register(customuser)