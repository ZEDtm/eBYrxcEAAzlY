from rest_framework import serializers
from .models import TgUser, TgFile


class TgUserSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = TgUser
        fields = ['fio', 'link']

    @staticmethod
    def get_link(obj):
        if obj.fio != '-':
            link = 'https://t.me/' + obj.fio
        else:
            link = None
        return link


class TgFileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = TgFile
        fields = ['name', 'url']

    @staticmethod
    def get_name(obj):
        file_name = obj.file.name.replace('files_message/', '')
        if len(file_name) > 32:
            file_name = file_name[:15] + '...' + file_name[-15:]
        return file_name

    @staticmethod
    def get_url(obj):
        return obj.file.url
