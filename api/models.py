from django.db import models


class PlaylistMembership(models.Model):
    order = models.IntegerField()
    track = models.ForeignKey('Track', on_delete=models.DO_NOTHING, related_name='playlists')
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, related_name='members')


class Track(models.Model):
    title = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)


class Playlist(models.Model):
    title = models.CharField(max_length=255)


class Receiver(models.Model):
    status = models.CharField(max_length=255, default='STOP')
    track = models.ForeignKey('Track', on_delete=models.DO_NOTHING, related_name='receivers')
