from django.db import models

# Create your models here.

class FixGroup(models.Model):
    name    = models.CharField(verbose_name='Название группы', max_length=32, unique=True)
    h_pwd   = models.BinaryField(max_length=64)
    token   = models.CharField(max_length=124, default='')
    a_name  = models.CharField(max_length=16, default='')
