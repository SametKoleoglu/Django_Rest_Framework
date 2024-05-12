from rest_framework import serializers
from news.models import *
from datetime import datetime
from django.utils.timesince import timesince



class NewsSerializer(serializers.ModelSerializer):
    broadcast_time = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'
        # exclude = ['updated_at']  buraya yazılan değerleri hariç tut !
        # sadece yazılanları okur.
        read_only_fields = ['id', 'release_date', 'updated_at']

    def broadcast_time(self, object):
        now = datetime.now()
        releae_date = object.release_date
        passing_time = timesince(releae_date, now)

        return passing_time

    # VALIDATIONS

    def validate(self, data):
        if data["title"] == data["content"]:
            raise serializers.ValidationError(
                "Title and Content cannot be same")

        return data

    def title_validate(self, title):
        if len(title) < 10:
            raise serializers.ValidationError("Title is too short")

        return title


class JournalistSerializer(serializers.ModelSerializer):
    news = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='news'
    )
    class Meta:
        model = Journalist
        fields = '__all__'