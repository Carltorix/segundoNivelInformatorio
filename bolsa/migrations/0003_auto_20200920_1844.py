# Generated by Django 3.1.1 on 2020-09-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0002_auto_20200917_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='fecha_caducacion',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='fecha_creado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='fecha_modificado',
            field=models.DateField(auto_now=True),
        ),
    ]