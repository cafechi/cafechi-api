from django.contrib import admin
from django.urls import path, include

from api.views import PlaylistList, PlaylistAddTrack, PlaylistDetail, ReceiverStatus, ReceiverCreate

urlpatterns = [
    path('playlist/', PlaylistList.as_view()),
    path('playlist/<int:pk>/', PlaylistDetail.as_view()),
    path('playlist/<int:pk>/add/<int:track_id>/', PlaylistAddTrack.as_view()),
    path('receiver/', ReceiverCreate.as_view()),
    path('receiver/<int:pk>/', ReceiverStatus.as_view())
]
