from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView

# Create your views here.

class ActorsView(ListView):
    template_name = "movie_app/all_actors.html"
    model = Actor


class DetailActorView(DetailView):
    template_name = "movie_app/one_actor.html"
    model = Actor
    # To use DetailView we have to point the parameter with the special name 'pk'(primary key) in urls.py
    # DetailView saves the needed data in 'context' variable with the name of the model but in lowercase. So we have to indicate this name in .html
    # # But we can change that by setting the needed variable
    # context_object_name = "our_name"


class DirectorsView(ListView):
    template_name = "movie_app/all_directors.html"
    model = Director


class DetailDirectorView(DetailView):
    template_name = "movie_app/one_directror.html"
    model = Director
    # To use DetailView we have to point the parameter with the special name 'pk'(primary key) in urls.py
    # DetailView saves the needed data in 'context' variable with the name of the model but in lowercase. So we have to indicate this name in .html
    # # But we can change that by setting the needed variable
    # context_object_name = "our_name"


# Functional way!

def show_all_movies(request):
    # movies = Movie.objects.order_by('name')
    # By using annotate we can create new columns by using SQL query
    # Value is needed to add new column in the table in the SQL query(not by creating new column in the table)
    movies = Movie.objects.annotate(new_field_bool=Value(True),
                                    new_field_false_boll=Value(False),
                                    new_budjet=F('budjet') + 100,
                                    )
    agg = movies.aggregate(Avg('budjet'), Max('year'), Avg('rating'))
    return render(request, 'movie_app/all_movies.html', {
        "movies": movies,
        "agg": agg
    })


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        "movie": movie
    })
#
#
# def show_all_directors(request):
#     directors = Director.objects.all()
#     return render(request, 'movie_app/all_directors.html', {
#         "directors": directors
#     })
#
#
# def show_one_director(request, director_id: int):
#     director = get_object_or_404(Director, id=director_id)
#     return render(request, 'movie_app/one_directror.html', {
#         "director": director
#     })


# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', {
#         "actors": actors
#     })


# def show_one_actor(request, actor_id):
#     actor = get_object_or_404(Actor, id=actor_id)
#     return render(request, 'movie_app/one_actor.html', {
#         "actor": actor
#     })



