# Generated by Django 3.2.4 on 2021-06-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
