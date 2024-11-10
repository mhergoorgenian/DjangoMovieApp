from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        #email=models.OneToOneField(User.email, on_delete=models.CASCADE)
        fullname=models.CharField( max_length=50,null=False,blank=False)

        def __str__(self):
            return self.user.username
