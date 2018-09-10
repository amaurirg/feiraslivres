from django.contrib import admin
from django.urls import path
from feiraslivres.core import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('feiraslivres/', views.FeirasLivresLista.as_view()),
    path('feiraslivres/<str:args1>/<str:args2>/', views.FeirasLivresBusca.as_view()),
    path('feiralivre/<str:registro>/', views.FeiraLivre.as_view()),
    path('popula_banco/', views.popula_banco),
]