from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator  # it's needed to limit the value range of a parameter


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_url(self):
        return reverse("director_detail", args=[self.id])


# For one-to-one links
class DressingRoom(models.Model):
    floor = models.IntegerField()
    cabin_number = models.IntegerField()

    def __str__(self):
        return f"{self.floor} {self.cabin_number}"


class Actor(models.Model):
    MALE = "M"
    FEMALE = "F"
    # It's needed for creation own Field
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    # For linking to the DrassingRoom table
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == "M":
            return f" Актёр {self.first_name} {self.last_name}"
        else:
            return f" Актриса {self.first_name} {self.last_name}"

    def get_url(self):
        return reverse("actor_detail", args=[self.id])


class Movie(models.Model):

    EUR = "EUR"
    USD = "USD"
    RUB = "RUB"
    # It's needed for creation own Field
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Ruble'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True)
    budjet = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default="", null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    # Making one-to-many link
    # related_name is needed for naming attribute for getting the information from the linked table
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name="movies")
    #Making many-to-many links
    actors = models.ManyToManyField(Actor, null=True, related_name="movies")

    # # if we don't have prepopulated_fields for filling slug in admin.py we have to use this method
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        # return f"{self.name} - {self.rating}% - {self.year} - {self.budjet}"
        return f"{self.name}"

    def get_url(self):
        return reverse("movie_detail", args=[self.slug])

# python manage.py shell_plus --print-sql