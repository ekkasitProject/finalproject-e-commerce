# Generated by Django 3.0 on 2021-02-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210211_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpending',
            name='silp',
        ),
        migrations.AddField(
            model_name='orderpending',
            name='slip',
            field=models.ImageField(blank=True, null=True, upload_to='slip'),
        ),
    ]