from song.models import Songs
from song.serializers import SongSerializer
from rest_framework import filters
from rest_framework import viewsets

class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all().order_by('Initial')
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Song_Name','Language','Singer']