from django.urls import path
from . import views

urlpatterns = [
    path('', views.ObsList.as_view(), name='panel'),
    path('recreate-entries/', views.recreate_entries, name='recreate-entries'),
    path('change-scene/<str:scene_name>/', views.change_scene, name='change_scene'),
    # path('active-scene/', views.active_scene, name='active_scene'),

]