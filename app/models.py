from django.db import models
from django.core import validators
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):

        return reverse('schooldetail',kwargs={'pk':self.pk})




class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=50)
    age=models.IntegerField() #validators=[validators.MinValueValidator(10),validators.MaxValueValidator(20)])

    def __str__(self) -> str:
        return self.sname