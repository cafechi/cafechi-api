from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.serializers import PlaylistSerializer, ReceiverSerializerCreate, ReceiverSerializerRetrieve, \
    ReceiverSerializerUpdate, TrackRetrieveSerializer


class TrackList(APIView):

    def get(self, request):
        tracks = models.Track.objects.all()
        serializer = TrackRetrieveSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TrackRetrieveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TrackDetail(APIView):
    pass


class PlaylistList(APIView):

    def get(self, request, **kwargs):
        pls = models.Playlist.objects.all()
        serializer = PlaylistSerializer(pls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistDetail(APIView):

    def get(self, request, pk):
        pl = models.Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(pl)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistAddTrack(APIView):

    def post(self, request, pk, track_id, **kwargs):
        existing_mem = models.PlaylistMembership.objects \
            .filter(playlist_id=pk) \
            .filter(track_id=track_id)

        if existing_mem:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        plm = models.PlaylistMembership.objects.create(playlist_id=pk, track_id=track_id, order=1)
        serializer = PlaylistSerializer(plm)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReceiverCreate(APIView):

    def post(self, request):
        serializer = ReceiverSerializerCreate(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReceiverStatus(APIView):

    def get(self, request, pk):
        receiver = models.Receiver.objects.get(pk=pk)
        serializer = ReceiverSerializerRetrieve(receiver)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        receiver = models.Receiver.objects.get(pk=pk)
        serializer = ReceiverSerializerUpdate(receiver, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
