# Generated by Django 3.2.8 on 2021-11-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='order',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='Quiz 01', max_length=100),
        ),
    ]