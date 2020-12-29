from django.contrib import admin
#Import all model
from .models import *

# Register your models here.
admin.site.register(Movie)