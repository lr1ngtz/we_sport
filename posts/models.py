from django.db import models

from django.contrib.auth.models import User

from core.models import BaseModel


class Post(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    topics = models.ManyToManyField("Topic")
    likes = models.PositiveIntegerField()
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Topic(BaseModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)


class Workout(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)


class Exercise(BaseModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    execution_time = models.TimeField(blank=True, null=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class ExerciseInfo(BaseModel):
    sets = models.PositiveSmallIntegerField(blank=True, null=True)
    reps = models.PositiveSmallIntegerField(blank=True, null=True)
    exercises = models.ManyToManyField(Exercise)


# class Comment(BaseModel):
#     # Maybe it's a good idea to move comments to the
#     # separate DB?
#
#     # owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
