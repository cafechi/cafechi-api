from rest_framework import serializers

from api import models


class TrackRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = ['id', 'title', 'resource_id', 'file', 'playlists']
        read_only_fields = ('resource_id', 'playlists')


class PlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackRetrieveSerializer(many=True)

    class Meta:
        model = models.Playlist
        fields = ['id', 'title', 'tracks']


class ReceiverSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Receiver
        fields = ['id', 'status']


class ReceiverSerializerRetrieve(serializers.ModelSerializer):
    track = TrackRetrieveSerializer()

    class Meta:
        model = models.Receiver
        fields = ['id', 'status', 'track']
        read_only_fields = ('status', 'track')


class ReceiverSerializerUpdate(serializers.ModelSerializer):
    track = serializers.PrimaryKeyRelatedField(queryset=models.Track.objects.all())

    # track = TrackRetrieveSerializer()

    class Meta:
        model = models.Receiver
        fields = ['id', 'status', 'track']
        # read_only_fields = ('track',)
