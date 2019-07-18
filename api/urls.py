from django.urls import path

from api.views import PlaylistList, PlaylistAddTrack, PlaylistDetail, ReceiverStatusUpdate, ReceiverCreate, TrackList

urlpatterns = [
    path('track/', TrackList.as_view()),
    path('playlist/', PlaylistList.as_view()),
    path('playlist/<int:pk>/', PlaylistDetail.as_view()),
    path('playlist/<int:pk>/add/<int:track_id>/', PlaylistAddTrack.as_view()),
    path('receiver/', ReceiverCreate.as_view()),
    path('receiver/<int:pk>/', ReceiverStatusUpdate.as_view())
]
