from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    student_id = models.IntegerField(verbose_name='شماره دانشجویی')
    is_student = models.BooleanField()


class Person(models.Model):
    national_id = models.IntegerField()
    age = models.IntegerField()
