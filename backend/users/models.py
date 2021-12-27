from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Users(models.Model):
    foreign_id = models.TextField(max_length=100)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    date_joined = models.DateField()
    date_of_birth = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
