# Generated by Django 3.0.5 on 2020-06-14 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_remove_player_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimitem',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='elo',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='blacks_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blacks_player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='whites_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whites_player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]