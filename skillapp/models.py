from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=50,null=True)
    # photo = models.ImageField(upload_to = 'profile/')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True)
    posts = models.ForeignKey('Posts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Section(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,null=True)
    subsribers = models.CharField(max_length=20)
    photo  = models.ImageField(upload_to = 'section/',null=True)

    def __str__(self):
        return self.name

    def new_section(self):
        self.save()

    def delete_section(self):
        self.delete()

class Posts(models.Model):
    title = models.CharField(max_length=60,null=True)
    description = models.CharField(max_length=100,null=True)
    question = models.TextField(max_length=400, null=True)
    section = models.ForeignKey(Section,related_name='Posts',null=True)
    # profile = models.ForeignKey('Profile', related_name='Posts',null=True)

    def __str__(self):
        return self.title

    def new_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Answers(models.Model):
    title = models.CharField(max_length=60,null=True)
    answer = models.TextField(max_length=200,null=True)

    def new_answer(self):
        self.save()

    def delete_answer(self):
        self.delete()