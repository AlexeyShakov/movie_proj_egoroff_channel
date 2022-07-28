from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budjet = models.IntegerField(default=1000000)
    slug = models.SlugField(default="", null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)



    def __str__(self):
        return f"{self.name} - {self.rating}% - {self.year} - {self.budjet}"

    def get_url(self):
        return reverse("movie_detail", args=[self.slug])