from django.urls import path
from . import views

#app_name = "polls"

urlpatterns = [
    path('', views.home, name='home'),
    path('GetAllHudumaView/', views.GetAllHudumaView.as_view(), name='GetAllHudumaView'),
    path('GetMgawanjoWaHudumaView/', views.GetMgawanjoWaHudumaView.as_view(), name='GetMgawanjoWaHudumaView'),
    path('GetAinaZaKukuView/', views.GetAinaZaKukuView.as_view(), name='GetAinaZaKukuView'),
    path('GetUmriWaKukuView/', views.GetUmriWaKukuView.as_view(), name='GetUmriWaKukuView'),
    path('GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView/', views.GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView.as_view(), name='GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView'),

   
        
]
