import requests

# API youtube 

def api_youtube(id):
    url = f'https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCG_Ib__3sibNQuSSK1-yp8bBQIp68qyLc&id={id}&part=snippet&part=contentDetails'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
