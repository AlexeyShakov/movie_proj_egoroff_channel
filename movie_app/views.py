from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director
# Create your views here.


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


def show_all_directors(request):
    directors = Director.objects.all
    return render(request, 'movie_app/all_directors.html', {
        "directors": directors
    })


def show_one_director(request, director_id: int):
    director = get_object_or_404(Director, id=director_id)
    return render(request, 'movie_app/one_directror.html', {
        "director": director
    })
