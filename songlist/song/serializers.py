from rest_framework import serializers
from song.models import Songs


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'

