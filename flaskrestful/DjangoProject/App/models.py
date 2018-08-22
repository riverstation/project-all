from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)


class Grade(models.Model):

    g_name = models.CharField(max_length=16)