from django.urls import path
from mywatchlist.views import show_movie, show_main
from mywatchlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_xml_by_id #sesuaikan dengan nama fungsi yang dibuat

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('html/', show_movie, name='show_movie'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]