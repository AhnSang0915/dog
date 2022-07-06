from django.db import models


# Create your models here.

# class Actors(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     date_of_birth = models.DateField(blank=True, null=True)

#     class Meta:
#         db_table = 'actor'


class Actors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(blank=True, null=True)
    movies = models.ManyToManyField(
        'Movies', related_name="owo"
        )

    class Meta:
        db_table = 'actor'


class Movies(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(blank=True, null=True)
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movie'


# class ActorsMovies(models.Model):
#     actor_id = models.ForeignKey(
#         'Actors', on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(
#         'Movies', on_delete=models.CASCADE
#     )

#     class Meta:
#         db_table = 'acmv'
