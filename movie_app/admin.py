from django.contrib import admin
from .models import Movie

# the decorator is needed to register our database table in admin panel
# for displaying additional columns in admin panel
@admin.register(Movie)
class Movie_admin(admin.ModelAdmin):
    # We put here the names of column to add
    list_display = ["name", "rating", "currency", "budjet", "rating_status"]
    # by using list_editable we can edit our data. We must delete the first
    # attribute list_display from list_editable as it is a LINK!!!!
    list_editable = ["rating", "currency", "budjet"]
    # ordering is needed for ordering our data
    ordering = ["-rating"]
    list_per_page = 3

    # This method is needed to add new column without creating them in database table
    # The decorator is needed for the column ability of being ordered
    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return f"Лучше не смотреть"
        if 50 <= movie.rating < 70:
            return f"Разок можно глянуть"
        if 70 <= movie.rating < 85:
            return f"Хороший фильм!"
        if movie.rating >= 85:
            return f"Фильм огонь!"

    # It's needed for creating new actions with data in admin panel
    def set_currency(self):
        pass

