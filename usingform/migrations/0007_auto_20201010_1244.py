# Generated by Django 3.0.6 on 2020-10-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usingform', '0006_defaultform_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultform',
            name='end_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='defaultform',
            name='start_at',
            field=models.DateField(null=True),
        ),
    ]
