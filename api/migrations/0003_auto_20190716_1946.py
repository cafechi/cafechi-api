# Generated by Django 2.2.3 on 2019-07-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190715_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='status',
        ),
        migrations.AlterField(
            model_name='playlistmembership',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='api.Playlist'),
        ),
    ]