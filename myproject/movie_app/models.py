from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MovieModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='movies')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name