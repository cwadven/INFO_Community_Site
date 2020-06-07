# Generated by Django 3.0.6 on 2020-06-05 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentalert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent', models.IntegerField(default=0)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]