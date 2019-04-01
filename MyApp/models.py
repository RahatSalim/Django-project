from django.db import models

# Create your models here.
class Emp(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=30)
    empsal = models.FloatField()
    empadd = models.CharField(max_length=30)
