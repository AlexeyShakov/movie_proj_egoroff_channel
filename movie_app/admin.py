from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet

class RatingFilter(admin.SimpleListFilter):

    title = "Фильтр по рейтингу"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        # The list of this values will be shown in the right side of the admin panel in the site
        return [
            ("<40", "Низкий"),
            ("от 40 до 59", "Средний"),
            ("от 60 до 84", "Высокий"),
            (">= 85", "Высочайший"),
                ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<40":
            return queryset.filter(rating__lt=40)
        elif self.value() == "от 40 до 59":
            return queryset.filter(rating__gte=40).filter(rating__lt=59)
        elif self.value() == "от 60 до 84":
            return queryset.filter(rating__gte=60).filter(rating__lt=84)
        else:
            return queryset.filter(rating__gte=85)


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
    actions = ["set_dollars", "set_rubles", "set_euros"]
    search_fields = ["name"]
    list_filter = ["name", "currency", RatingFilter]

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
    # Queryset is related with ORM
    @admin.action(description="Установить валюту в доллар")
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description="Установить валюту в рубли")
    def set_rubles(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.RUB)

    @admin.action(description="Установить валюту в евро")
    def set_euros(self, request, queryset: QuerySet):
        # Returns the amount of rows updated
        count_updated = queryset.update(currency=Movie.EUR)
        self.message_user(request, message=f"Было обновлено {count_updated} записей")