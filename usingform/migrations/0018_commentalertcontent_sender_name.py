# Generated by Django 3.0.6 on 2020-06-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usingform', '0017_auto_20200605_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentalertcontent',
            name='sender_name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]