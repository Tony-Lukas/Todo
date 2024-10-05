# Generated by Django 4.2.16 on 2024-10-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_items',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='todo_items',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
