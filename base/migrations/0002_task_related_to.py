# Generated by Django 4.2.2 on 2023-06-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='related_to',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
