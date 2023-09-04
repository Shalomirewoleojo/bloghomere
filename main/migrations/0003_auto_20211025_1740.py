# Generated by Django 3.2.8 on 2021-10-25 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211022_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogcreate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogcreate',
            name='description',
            field=models.CharField(blank=True, default='This is a blog', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogcreate',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
