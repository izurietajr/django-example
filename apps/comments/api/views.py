from rest_framework import generics

from apps.comments.models import Entity

from apps.comments.api.serializers import EntitySerializer, EntityUpdateSerializer


class EntityList(generics.ListAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityUpdate(generics.UpdateAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntityUpdateSerializer


class EntityCreate(generics.CreateAPIView):

    serializer_class = EntityUpdateSerializer
