from django.urls import path
from . import views
urlpatterns = [
    path('voluntarios', views.VoluntarioView.as_view(), name='voluntarios',),
    path('voluntarios/<int:id>/', views.VoluntarioView.as_view(), name='voluntarios',),

    path('', views.EventoView.as_view(), name='eventos',),
    path('eventos/<int:id>/', views.EventoView.as_view(), name='eventos',),
]
