# Generated by Django 4.2.6 on 2023-10-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
