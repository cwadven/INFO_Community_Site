# Generated by Django 3.0.6 on 2020-06-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
