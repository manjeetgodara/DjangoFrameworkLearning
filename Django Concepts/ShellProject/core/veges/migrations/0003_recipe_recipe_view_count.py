# Generated by Django 4.2.6 on 2023-10-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veges', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]