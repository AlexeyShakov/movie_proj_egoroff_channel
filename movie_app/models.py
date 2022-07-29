from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budjet = models.IntegerField(default=1000000)
    slug = models.SlugField(default="", null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)



    def __str__(self):
        # return f"{self.name} - {self.rating}% - {self.year} - {self.budjet}"
        return f"{self.name}"

    def get_url(self):
        return reverse("movie_detail", args=[self.slug])