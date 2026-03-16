
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DogPark

@api_view(["GET"])
def parks(request):
    return Response(list(DogPark.objects.values()))
