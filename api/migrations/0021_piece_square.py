# Generated by Django 3.0.5 on 2020-06-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_auto_20200615_1851"),
    ]

    operations = [
        migrations.AddField(
            model_name="piece",
            name="square",
            field=models.CharField(
                choices=[
                    (0, "A1"),
                    (1, "B1"),
                    (2, "C1"),
                    (3, "D1"),
                    (4, "E1"),
                    (5, "F1"),
                    (6, "G1"),
                    (7, "H1"),
                    (8, "A2"),
                    (9, "B2"),
                    (10, "C2"),
                    (11, "D2"),
                    (12, "E2"),
                    (13, "F2"),
                    (14, "G2"),
                    (15, "H2"),
                    (16, "A3"),
                    (17, "B3"),
                    (18, "C3"),
                    (19, "D3"),
                    (20, "E3"),
                    (21, "F3"),
                    (22, "G3"),
                    (23, "H3"),
                    (24, "A4"),
                    (25, "B4"),
                    (26, "C4"),
                    (27, "D4"),
                    (28, "E4"),
                    (29, "F4"),
                    (30, "G4"),
                    (31, "H4"),
                    (32, "A5"),
                    (33, "B5"),
                    (34, "C5"),
                    (35, "D5"),
                    (36, "E5"),
                    (37, "F5"),
                    (38, "G5"),
                    (39, "H5"),
                    (40, "A6"),
                    (41, "B6"),
                    (42, "C6"),
                    (43, "D6"),
                    (44, "E6"),
                    (45, "F6"),
                    (46, "G6"),
                    (47, "H6"),
                    (48, "A7"),
                    (49, "B7"),
                    (50, "C7"),
                    (51, "D7"),
                    (52, "E7"),
                    (53, "F7"),
                    (54, "G7"),
                    (55, "H7"),
                    (56, "A8"),
                    (57, "B8"),
                    (58, "C8"),
                    (59, "D8"),
                    (60, "E8"),
                    (61, "F8"),
                    (62, "G8"),
                    (63, "H8"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
