from django.urls import path
from . import views
from .views import ActorsView, DetailActorView, DirectorsView, DetailDirectorView

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    # path('directors', views.show_all_directors),
    path('directors', views.DirectorsView.as_view()),
    # path('directors/<int:director_id>', views.show_one_director, name='director_detail'),
    path('directors/<int:pk>', views.DetailDirectorView.as_view(), name='director_detail'),
    # path('actors', views.show_all_actors),
    path('actors/', views.ActorsView.as_view()),
    # path('actors/<int:actor_id>', views.show_one_actor, name="actor_detail"),
    path('actors/<int:pk>', views.DetailActorView.as_view(), name="actor_detail"),

]
