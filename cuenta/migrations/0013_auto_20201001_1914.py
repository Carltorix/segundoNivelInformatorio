# Generated by Django 3.1.1 on 2020-10-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0012_auto_20201001_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='que_hacemos',
            name='para_que_te_sirve',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='que_hacemos',
            name='que_hacemos',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='que_hacemos',
            name='que_podes_hacer',
            field=models.TextField(default='', max_length=300),
        ),
    ]