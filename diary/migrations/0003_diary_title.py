# Generated by Django 3.0.4 on 2020-03-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200322_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]