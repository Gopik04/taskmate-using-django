# Generated by Django 5.1.3 on 2024-12-28 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_rename_manager_tasklist_manage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='manage',
        ),
    ]
