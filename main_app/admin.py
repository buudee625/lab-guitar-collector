from django.contrib import admin

# Register your models here.
from .models import Guitar, Review
admin.site.register(Guitar)
admin.site.register(Review)