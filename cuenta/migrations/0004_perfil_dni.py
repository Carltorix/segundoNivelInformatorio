# Generated by Django 3.1.1 on 2020-09-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_auto_20200917_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='dni',
            field=models.CharField(default='0000000000', max_length=10, unique=True),
        ),
    ]