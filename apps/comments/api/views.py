from rest_framework import generics

from apps.comments.models import Entity

from apps.comments.api.serializers import EntitySerializer


class EntityList(generics.ListAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
