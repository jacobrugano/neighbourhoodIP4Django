from django.contrib import admin

# Register your models here.
from .models import Neighborhood, Profile, Business, Post

admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)