from django.db import models

# Create your models here.

class Video(models.Model):
    youtube_id = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo if self.titulo else self.youtube_id
