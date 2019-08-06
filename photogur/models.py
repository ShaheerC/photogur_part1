from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class Picture(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.CharField(max_length=255, validators=[URLValidator()])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return (f"{self.title} by {self.artist}")

class PictureForm(ModelForm):

    class Meta:
        model = Picture
        fields = ['title', 'artist', 'url']

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')