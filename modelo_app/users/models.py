import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    rfc = models.CharField(max_length=100)
    photo = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

class User_Adress (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    zip_code = models.IntegerField(null=True, default=None)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.street