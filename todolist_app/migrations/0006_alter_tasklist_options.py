# Generated by Django 5.1.3 on 2024-12-29 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_tasklist_manage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ['id']},
        ),
    ]
