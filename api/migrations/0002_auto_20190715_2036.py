# Generated by Django 2.2.3 on 2019-07-15 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistmembership',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='api.Playlist'),
        ),
        migrations.AlterField(
            model_name='playlistmembership',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='playlists', to='api.Track'),
        ),
    ]
