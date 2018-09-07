from django.contrib import admin
from django.urls import path
from feiraslivres.core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feiraslivres/', views.FeirasLivresLista.as_view()),
    path('feiralivre/<int:pk>/', views.FeiraLivre.as_view()),
]