# Generated by Django 4.1 on 2022-08-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0009_landingpageentry_notes_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="landingpageentry",
            name="notes_first_added",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
