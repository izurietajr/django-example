from rest_framework import serializers

from apps.comments.models import Entity, Comment, Score


class EntitySerializer(serializers.ModelSerializer):

    class Meta:

        model = Entity
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = '__all__'

 class ScoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Score
        fields = '__all__'
