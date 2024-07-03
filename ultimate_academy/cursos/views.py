from django.shortcuts import render
import requests
from .models import Video
from .api import api_youtube

def index(request):
    return render(request, 'ultimate_academy/index.html')

def cursos(request):
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
            'duracion': video_info['contentDetails']['duration'],
            'fecha_publicacion': video_info['snippet']['publishedAt'],
            'miniatura': video_info['snippet']['thumbnails']['high']['url'],
        }
        # Agrego el diccionario a la lista 'videos_info'
        videos_info.append(video_data)
     

    context = {
        'videos': videos_info,
        'ids': ids,
    }
        

    return render(request, 'ultimate_academy/cursos.html', context)

def filtrar_duracion(parametro):
    '''Funcion que toma como parametro un string dado de la API y modifica lo vista de la duracion del tiempo del video'''
    duracion = ''
    numbers = '0123456789'
    for i in parametro:
        if i in numbers:
            duracion += i
        elif i == 'H':
            duracion += 'h:'
        elif i == 'M':
            duracion += 'm:'
        elif i == 'S':
            duracion += 's'
        else: 
            continue
    
    return duracion