from rest_framework import serializers

from apps.comments.models import Entity, Comment, Score



class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Score
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    score_list = ScoreSerializer(many=True)

    class Meta:

        model = Entity
        fields = ['name', 'description', 'comments', 'score_list', 'id']

