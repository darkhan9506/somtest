# Generated by Django 2.1.5 on 2019-01-27 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('code', models.IntegerField(verbose_name='Код')),
                ('position', models.CharField(blank=True, default='', max_length=100, verbose_name='Должность')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Departments')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Employees')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='departments',
            field=models.ManyToManyField(blank=True, through='testapp.Membership', to='testapp.Departments', verbose_name='Подразделения'),
        ),
    ]
