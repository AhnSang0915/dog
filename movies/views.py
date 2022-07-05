import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actors, Movies, ActorsMovies

class ActorsView(View):
    def get(self, request):
        actors = Actors.objects.all()
        results = []

        for actor in actors:
            results.append(
                {
                    "first_name" : actors.first_name,
                    "last_name" : actors.last_name,
                    "date_of_birth" : actors.date_of_birth,
                    "movies" : 
                }
            )
