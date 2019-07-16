from rest_framework import serializers

from api import models


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = ['id', 'title', 'resource_id']


class PlMembership(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = models.PlaylistMembership
        fields = ['order', 'playlist', 'track']


class PlaylistSerializer(serializers.ModelSerializer):
    members = PlMembership(many=True)

    class Meta:
        model = models.Playlist
        fields = ['id', 'title', 'members']


class ReceiverSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = models.Receiver
        fields = ['id', 'status']


class ReceiverSerializerRetrieve(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = models.Receiver
        fields = ['id', 'status', 'track']


class ReceiverSerializerUpdate(serializers.ModelSerializer):
    track = serializers.PrimaryKeyRelatedField(queryset=models.Track.objects.all())

    class Meta:
        model = models.Receiver
        fields = ['id', 'status', 'track']
