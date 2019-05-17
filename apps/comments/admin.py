from django.contrib import admin

# Register your models here.
from apps.comments.models import Entity, Comment, Score

admin.site.register(Entity)
admin.site.register(Comment)
admin.site.register(Score)
