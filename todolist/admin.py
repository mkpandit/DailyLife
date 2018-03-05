from django.contrib import admin

# Register your models here.
from .models import to_do_list
admin.site.register(to_do_list)