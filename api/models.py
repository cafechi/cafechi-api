from django.db import models


class PlaylistMembership(models.Model):
    track = models.ForeignKey('Track', on_delete=models.CASCADE, related_name='playlists')
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'PlMembership({self.id})<pl:{self.playlist.title},track:{self.track.title},order:{self.order}>'


class Track(models.Model):
    title = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return f'Track({self.id})<title:{self.title},resource_id:{self.resource_id},file:{self.file.name}>'


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    tracks = models.ManyToManyField('Track', through='PlaylistMembership')

    def __str__(self):
        return f'Playlist({self.id})<title:{self.title}>'


class Receiver(models.Model):
    status = models.CharField(max_length=255, default='STOP')
    track = models.ForeignKey('Track', on_delete=models.DO_NOTHING, related_name='receivers',
                              default=Track.objects.first())

    def __str__(self):
        return f'Receiver({self.id})<status:{self.status},track:{self.track_id}>'
