from django.db import models

# Create your models here.

class School(models.Model):
    schoolname = models.CharField(max_length=100)
    schoollogo = models.ImageField(upload_to='school/images')
    schoolurl = models.URLField(blank=True)

    def __str__(self):
        return self.schoolname


class Interest(models.Model):
    interest = models.CharField(max_length=100)
    image = models.ImageField(upload_to='interest/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.interest


class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=100)
    socialtext = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name