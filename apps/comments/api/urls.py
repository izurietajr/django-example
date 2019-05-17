from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from apps.comments.api.views import EntityList, EntityDetail, EntityUpdate, EntityCreate

namespace='comments_api'
urlpatterns = [
    path('entities/', EntityList.as_view(), name='entities_list'),
    path('entity/<pk>/details/', EntityDetail.as_view(), name='entity_detail'),
    path('entity/<pk>/update/', EntityUpdate.as_view(), name='entity_update'),
    path('entity/create/', EntityCreate.as_view(), name='entity_create'),
]