# Generated by Django 4.1 on 2022-08-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registered_dttm',
            field=models.DateTimeField(auto_now_add=True, verbose_name='회원가입 시점'),
        ),
    ]