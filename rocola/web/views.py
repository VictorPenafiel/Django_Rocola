from django.shortcuts import render
from web.models import *
from web.forms import MainForm
from django.http import JsonResponse

def index(request):
    track_datos = Track.objects.all()
    if request.method == 'POST': #Formulario manipulado por el usuario
        forma = MainForm(request.POST)
        artista_buscado = request.POST.get('artista_selector')
        album_buscado = request.POST.get('album_selector')
        print(artista_buscado,album_buscado)
    
        if album_buscado != '':
            track_datos = track_datos.filter(album_id = album_buscado) 
            
    else:
        forma = MainForm()
        track_datos = []
    return render(request, 'form.html', {'tracks': track_datos, 'form': forma})

def getalbums(request):
    if request.method == "POST":
        artist__id = request.POST['artist_id']
        data = {}
        try:
            album = Album.objects.filter(artist_id=artist__id)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(album.values('album_id', 'title')), safe = False)



def detalle(request):
    codigo_track = request.POST.get('detalle_id')
    print(codigo_track)
    query = """
        SELECT
            T.track_id,
            T.name AS cancion,
            T.composer AS compositor,
            AL.title AS album_nombre,
            AR.name AS artista
        FROM
            track AS T
        JOIN
            album AS AL ON AL.album_id = T.album_id
        JOIN
            artist AS AR ON AR.artist_id = AL.artist_id
        WHERE
            T.track_id = %s;
    """
    datos = Track.objects.raw(query, [codigo_track])

    if datos:
        return render(request, 'detalle.html', {'datos': datos[0]})
    else:
        return render(request, 'error.html', {'mensaje': 'El track no fue encontrado.'})
    
