# Generated by Django 3.2.8 on 2021-10-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
