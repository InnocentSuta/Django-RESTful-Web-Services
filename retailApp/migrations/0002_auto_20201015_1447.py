# Generated by Django 3.1.2 on 2020-10-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
