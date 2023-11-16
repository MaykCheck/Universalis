from django.urls import path
from mapapp import views

app_name = 'mapapp'

urlpatterns = [
    path('',views.anasayfa,
         name='anasayfa'),
]