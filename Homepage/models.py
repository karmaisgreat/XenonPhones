from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser, models.Model):
    email = models.EmailField(unique = True)

class Phones(models.Model):
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='phones', default='phones/default_phone.png')
    model_no = models.CharField(max_length=255, unique=True)
    processor = models.CharField(max_length=255, blank=True)
    price = models.PositiveIntegerField(blank=True)
    phone_os = models.CharField(max_length=100, blank=True)
    ram = models.PositiveIntegerField(blank=True)


    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name = 'Phones'
        verbose_name_plural = 'Phones'


class ContactFeedback(models.Model):
    full_name=models.CharField(max_length=255,null=True,blank=True)
    contact_num=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    subject=models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField()


    def save(self, *args, **kwargs):
        if not self.full_name :
                user=f"Anonymous User"
                self.full_name = user
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = 'Feedbacks'
        verbose_name_plural = 'Feedbacks'