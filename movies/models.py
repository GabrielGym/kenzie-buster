from django.db import models


class Movie_ratings(models.TextChoices):
    Rated_G = "G"
    Rated_PG = "PG"
    Rated_PG_13 = "PG-13"
    Rated_R = "R"
    Rated_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=Movie_ratings.choices,
        default=Movie_ratings.Rated_G,
        null=True,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey('movies.Movie',on_delete=models.CASCADE, related_name='moviesOrder')
    user = models.ForeignKey('users.User',on_delete=models.CASCADE, related_name='moviesOrder')
