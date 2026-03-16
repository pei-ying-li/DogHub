
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dog

@api_view(["GET"])
def dogs(request):
    return Response(list(Dog.objects.values()))
