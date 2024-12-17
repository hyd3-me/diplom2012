from django.db import models
from django.contrib.auth.models import User

from app_fixgroups.models import FixGroup

# Create your models here.

class ControlDate(models.Model):

    name    = models.CharField(verbose_name='наименование товара', max_length=64)
    c_date  = models.DateField(auto_now_add=True)
    e_date  = models.DateTimeField(verbose_name='окончание срока')
    owner   = models.ForeignKey(User, on_delete=models.PROTECT)
    group   = models.ForeignKey(FixGroup, on_delete=models.CASCADE)
