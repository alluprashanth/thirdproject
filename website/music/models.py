from django.db import models
from django.core.urlresolvers import reverse
class Album(models.Model):
    artist=models.CharField(max_length=300)
    album_title=models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    album = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('music:details', )

    def __str__(self):
        return self.artist+' '+self.album_title
class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type= models.CharField(max_length=300)
    song_title= models.CharField(max_length=300)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title