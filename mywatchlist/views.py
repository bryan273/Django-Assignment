from django.shortcuts import render
from mywatchlist.models import MovieItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_movie(request):
    data_barang_movie = MovieItem.objects.all()
    context = {
        'list_movie': data_barang_movie,
        'nama': 'Bryan Tjandra'
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = MovieItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = MovieItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MovieItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = MovieItem.objects.filter(pk=id)
    # return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")