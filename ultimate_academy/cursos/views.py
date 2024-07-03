from django.shortcuts import render
import requests

def index(request):
    return render(request, 'ultimate_academy/index.html')

def cursos(request):
    # Url de la API para la consulta del video PYTHON de SOYDALTO 
    url = f'https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCG_Ib__3sibNQuSSK1-yp8bBQIp68qyLc&id=nKPbfIU442g&part=snippet&part=contentDetails'
    # Realizamos la consulta a la API
    response = requests.get(url)

    if response.status_code == 200:
        # Obtenemos el contenido de la respuesta
        data = response.json()
        video_info = data['items'][0]

        # Filtro la información que necesito 

        titulo_video = video_info['snippet']['title']
        duracion_video_sin_filtrar = video_info['contentDetails']['duration']
        fecha_publicacion_video = video_info['snippet']['publishedAt']
        miniatura_video = video_info['snippet']['thumbnails']['high']['url']
        duracion_video = filtrar_duracion(duracion_video_sin_filtrar)

        context = {'titulo' : titulo_video, 'duracion': duracion_video, 'fecha_publicacion': fecha_publicacion_video, 'miniatura': miniatura_video}
        

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