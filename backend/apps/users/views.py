
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile

@api_view(["GET"])
def profile(request):
    profile = UserProfile.objects.first()
    if not profile:
        return Response({"message": "no profile"})
    return Response({
        "user": profile.user.username,
        "city": profile.city,
        "bio": profile.bio
    })
