# Generated by Django 2.2.3 on 2019-07-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190716_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='token',
        ),
        migrations.AddField(
            model_name='receiver',
            name='status',
            field=models.CharField(default='STOP', max_length=255),
        ),
    ]
