from django.shortcuts import render
import requests
from .models import Video
from .api import api_youtube

def index(request):
    return render(request, 'ultimate_academy/index.html')

def cursos(request):
    '''Vista principal que retorna todos los cursos precargados'''
    # Traigo todos los Ids existentes en la BBDD
    ids = Video.objects.values_list('youtube_id', flat=True)

    videos_info = []

    # Creo un bucle que lea por Ids 
    for id in ids:
        data = api_youtube(id)
        video_info = data['items'][0]

        # Almaceno la información en un diccionario 

        video_data = {
            'titulo': video_info['snippet']['title'],
            'fecha_publicacion': video_info['snippet']['publishedAt'],
            'miniatura': video_info['snippet']['thumbnails']['high']['url'],
            'id': video_info['id'],
        }
        # Agrego el diccionario a la lista 'videos_info'
        videos_info.append(video_data)
     

    context = {
        'videos': videos_info,
        'ids': ids,
    }
        

    return render(request, 'ultimate_academy/cursos.html', context)


def clase(request, youtube_id):
    data = api_youtube(youtube_id)
    video_info = data['items'][0]

    video_data = {
        'titulo': video_info['snippet']['title'],
        'duracion': video_info['contentDetails']['duration'],
        'fecha_publicacion': video_info['snippet']['publishedAt'],
        'miniatura': video_info['snippet']['thumbnails']['high']['url'],
        'id': video_info['id'],
    }

    context = {
        'clase': video_data,
    }
    return render(request, 'ultimate_academy/clase.html', context)