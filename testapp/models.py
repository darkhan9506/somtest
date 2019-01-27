from django.db import models

# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подразделения')


class Employees(models.Model):
    photo = models.ImageField(verbose_name='Фото')
    code = models.IntegerField(verbose_name='Код')
    position = models.CharField(max_length=100, verbose_name='Должность', blank=True, default='')
    name = models.CharField(max_length=100, verbose_name='ФИО')
    departments = models.ManyToManyField(Departments, blank=True, through='Membership', verbose_name='Подразделения')


class Membership(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)


