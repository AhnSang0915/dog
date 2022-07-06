import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actors, Movies

class ActorsView(View):
    def get(self, request):
        actors = Actors.objects.all()
        results=[]
        for actor in actors:
            movies = actor.movies.all()
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "movies" : [i.title for i in [movie for movie in movies]]
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class MoviesView(View):
    def get(self, request):
        movies = Movies.objects.all()
        results=[]
        for movie in movies:
            actors = movie.owo.all()
            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "actors" : [i.first_name for i in [actor for actor in actors]]
                }
            )
        return JsonResponse({'resutls':results}, status=200)