# Generated by Django 3.2.8 on 2021-11-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='numofpages',
            field=models.IntegerField(default=200),
        ),
    ]
