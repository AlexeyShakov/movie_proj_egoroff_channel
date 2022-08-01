from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors', views.show_all_directors),
    path('directors/<int:director_id>', views.show_one_director, name='director_detail'),
    path('actors', views.show_all_actors),
    path('actors/<int:actor_id>', views.show_one_actor, name="actor_detail"),
]
