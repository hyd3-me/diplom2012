from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FixGroup(models.Model):
    name    = models.CharField(verbose_name='Название группы', max_length=32, unique=True)
    h_pwd   = models.BinaryField(max_length=64)
    token   = models.CharField(max_length=124, default='')
    a_name  = models.CharField(max_length=16, default='')
    owner   = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

class Staff(models.Model):

    RANK = (
        (0, 'Гость'),
        (1, 'Мерч/Кас'),
        (2, 'Админ'),
        (7, 'su'),
        )

    group   = models.ForeignKey(
        FixGroup, on_delete=models.CASCADE, null=True, blank=True)
    user    = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    rank    = models.PositiveSmallIntegerField(
                choices=RANK,
                default=0)

    
