from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog,
        'nama': 'Bryan Tjandra'
    }
    return render(request, "katalog.html", context)
