# Generated by Django 3.2 on 2022-10-31 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='Favorite',
            field=models.BooleanField(default=True),
        ),
    ]
