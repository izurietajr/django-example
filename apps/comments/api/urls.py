from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from apps.comments.api.views import EntityList

namespace='comments_api'
urlpatterns = [
    path('entities/', EntityList.as_view(), name='entities_list')
]