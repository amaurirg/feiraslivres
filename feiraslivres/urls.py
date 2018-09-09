from django.contrib import admin
from django.urls import path
from feiraslivres.core import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('feiraslivres/', views.FeirasLivresLista.as_view()),
    path('feiralivre/<str:registro>/', views.FeiraLivre.as_view()),
]