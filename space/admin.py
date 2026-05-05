from django.contrib import admin
from .models import SpacePost, Category

# CustomUser ni bu yerdan olib tashladik, chunki u models.py da yo'q
admin.site.register(SpacePost)
admin.site.register(Category)
