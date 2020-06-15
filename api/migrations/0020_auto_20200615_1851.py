# Generated by Django 3.0.5 on 2020-06-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200615_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='description',
            new_name='termination',
        ),
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.TextField(choices=[('White wins', 'White wins'), ('Black wins', 'Black wins'), ('Draw', 'Drawn game'), ('In progress', 'Game still in progress, game abandoned, or result otherwise unknown')], default='In progress'),
        ),
    ]
