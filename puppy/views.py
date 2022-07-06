import json

from django.http import JsonResponse
from django.views import View

from puppy.models import Owners, Dogs

# Create your views here.
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owners.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        owners = Owners.objects.all()
        dogs = Dogs.objects.all()
        result = []

        for owner in owners:
            for dog in dogs:
                if owner.id == dog.owner_id:
                    result.append({
                        "name" : owner.name,
                        "age" : owner.age,
                        "email" : owner.email,
                        "my_dog": {"dog" : dog.name,
                        "dog_age" : dog.age}
                    })
        return JsonResponse({'results' : result}, status=200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dogs.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owners.objects.get(name=data['owner'])
        )
        return JsonResponse({'message':'created'}, status=201)
         
    def get(self, request):
        dogs = Dogs.objects.all()
        result = []
        for dog in dogs:
                result.append({
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name,
                })
        return JsonResponse({'results' : result}, status=200)