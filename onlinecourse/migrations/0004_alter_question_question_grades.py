# Generated by Django 3.2.7 on 2022-03-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20220312_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_grades',
            field=models.IntegerField(),
        ),
    ]
