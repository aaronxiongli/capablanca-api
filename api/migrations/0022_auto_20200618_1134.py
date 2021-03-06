# Generated by Django 3.0.7 on 2020-06-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_piece_square"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="castling_rights",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="board",
            name="ep_square",
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="board",
            name="fullmove_number",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="board",
            name="halfmove_clock",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="board", name="turn", field=models.IntegerField(null=True),
        ),
    ]
