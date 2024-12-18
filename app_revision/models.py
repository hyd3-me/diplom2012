from django.db import models

from app_fixgroups.models import FixGroup


# Create your models here.

class Revision(models.Model):

    name = models.DateField(verbose_name='дата ревизии')
    group = models.ForeignKey(FixGroup, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False, verbose_name='архив')

    class Meta:
        ordering = ['-name']

class List(models.Model):

    name = models.CharField(verbose_name='имя списка', max_length=32)
    revision = models.ForeignKey(Revision, on_delete=models.CASCADE)
