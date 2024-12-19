from django.db import models

from app_fixgroups.models import FixGroup, Staff


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

class Record(models.Model):

    name = models.CharField(verbose_name='имя записи', max_length=64)
    barcode = models.CharField(verbose_name='баркод', max_length=32)
    count = models.PositiveSmallIntegerField(verbose_name='количество')
    owner = models.ForeignKey(Staff, on_delete=models.PROTECT)
    _list = models.ForeignKey(List, on_delete=models.CASCADE)
    note = models.TextField(verbose_name='добавить примечание', max_length=124, blank=True)
