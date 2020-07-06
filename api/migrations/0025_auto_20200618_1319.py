# Generated by Django 3.0.7 on 2020-06-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0024_board_castling_rights"),
    ]

    operations = [
        migrations.RemoveField(model_name="move", name="piece",),
        migrations.AddField(
            model_name="move",
            name="board",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="api.Board"
            ),
        ),
    ]
