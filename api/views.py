from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response

from api import models
from api.serializers import PlaylistSerializer, ReceiverSerializerCreate, ReceiverSerializerUpdate, \
    TrackRetrieveSerializer, ReceiverSerializerRetrieve


class TrackList(generics.GenericAPIView):

    def get(self, request):
        tracks = models.Track.objects.all()
        serializer = TrackRetrieveSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TrackRetrieveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TrackDetail(generics.GenericAPIView):
    pass


class PlaylistList(generics.GenericAPIView):

    def get(self, request, **kwargs):
        pls = models.Playlist.objects.all()
        serializer = PlaylistSerializer(pls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistDetail(generics.GenericAPIView):

    def get(self, request, pk):
        pl = models.Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(pl)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistAddTrack(generics.GenericAPIView):

    def post(self, request, pk, track_id, **kwargs):
        existing_mem = models.PlaylistMembership.objects \
            .filter(playlist_id=pk) \
            .filter(track_id=track_id)

        if existing_mem:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        plm = models.PlaylistMembership.objects.create(playlist_id=pk, track_id=track_id, order=1)
        serializer = PlaylistSerializer(plm)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReceiverCreate(generics.CreateAPIView):
    queryset = models.Receiver.objects.all()
    serializer_class = ReceiverSerializerCreate


class ReceiverStatusUpdate(views.APIView):
    queryset = models.Receiver.objects.all()
    serializer_class = ReceiverSerializerUpdate

    def get(self, request, pk):
        instance = self.queryset.get(pk=pk)
        if instance:
            ser = ReceiverSerializerRetrieve(instance)
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = ReceiverSerializerUpdate(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ReceiverStatusRetrieve(generics.RetrieveAPIView):
    queryset = models.Receiver.objects.all()
    serializer_class = ReceiverSerializerRetrieve
