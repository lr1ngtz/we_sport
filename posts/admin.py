from django.contrib import admin

from posts.models import (
    Post,
    Topic,
    Workout,
    Exercise,
    ExerciseInfo,
    Comment,
    Like,
    Dislike,
)


admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(ExerciseInfo)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
