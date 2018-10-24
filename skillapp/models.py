from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=50)
    photo  = models.ImageField(upload_to = 'profile/')

    def __str__(self):
        return self.bio

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Section(models.Model):
    name = models.CharField(max_length=50)
    subsribers = models.CharField(max_length=20)
    admin = models.ForeignKey('Profile', related_name='Section',null=True)

    def __str__(self):
        return self.name

    def new_section(self):
        self.save()

    def delete_section(self):
        self.delete()

class Question(models.Model):
    question = models.TextField(max_length=100)