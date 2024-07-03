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
        titulo_descripcion = video_info['snippet']['description']
        duracion_video = video_info['contentDetails']['duration']
        fecha_publicacion_video = video_info['snippet']['publishedAt']
        vistas_video = video_info['statics']['viewCount']




    return render(request, 'ultimate_academy/cursos.html')