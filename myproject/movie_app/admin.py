from django.contrib import admin
from .models import AuthorModel,CategoryModel,MovieModel
# Register your models here.
admin.site.register(MovieModel)
admin.site.register(CategoryModel)
admin.site.register(AuthorModel)