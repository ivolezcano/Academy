from django.shortcuts import render
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def clase(request, youtube_id):
    if request.method == "POST":
        try:
            datos = json.loads(request.body)
            dato = datos.get('dato') 
            request.session['dato_post'] = dato
            response = {'status': 'success', 'message': 'Dato recibido correctamente', 'dato': dato}
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Datos JSON inválidos'}, status=400)
    else:
        data = api_youtube(youtube_id)
        video_info = data['items'][0]

        dato_post = request.session.get('dato_post', '')

        video_data = {
            'titulo': video_info['snippet']['title'],
            'duracion': video_info['contentDetails']['duration'],
            'fecha_publicacion': video_info['snippet']['publishedAt'],
            'miniatura': video_info['snippet']['thumbnails']['high']['url'],
            'id': video_info['id'],
        }

        video_link = f'https://www.youtube.com/watch?v={youtube_id}'

        context = {
            'clase': video_data,
            'link': video_link,
            'dato_post': dato_post, 
        }
        return render(request, 'ultimate_academy/clase.html', context)