# Generated by Django 2.0.4 on 2018-06-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180619_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo',
            field=models.URLField(default='#', verbose_name='Repositorio'),
        ),
    ]
