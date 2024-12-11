# Generated by Django 4.2.17 on 2024-12-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FixGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название группы')),
                ('h_pwd', models.BinaryField(max_length=64)),
                ('token', models.CharField(default='', max_length=124)),
                ('a_name', models.CharField(default='', max_length=16)),
            ],
        ),
    ]