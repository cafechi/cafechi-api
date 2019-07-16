# Generated by Django 2.2.3 on 2019-07-16 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190716_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='track',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receivers', to='api.Track'),
            preserve_default=False,
        ),
    ]
