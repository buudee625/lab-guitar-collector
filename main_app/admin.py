from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Guitar)
admin.site.register(Review)
admin.site.register(Player)