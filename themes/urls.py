from django.urls import path
from .views import themes_list,theme_detail

urlpatterns = [
    path('',themes_list,name='themes_list'),
    path('<int:pk>/',theme_detail,name='theme_detail')
]