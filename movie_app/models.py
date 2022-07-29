from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator  # it's needed to limit the value range of a parameter

# Create your models here.

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

    # # if we don't have prepopulated_fields for filling slug in admin.py we have to use this method
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        # return f"{self.name} - {self.rating}% - {self.year} - {self.budjet}"
        return f"{self.name}"

    def get_url(self):
        return reverse("movie_detail", args=[self.slug])