from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class UsersApiView(APIView):
    def get(self, request):
        """
        Return a list of all users.
        """
        usernames = [{'name': user.name, "email": user.email, "password": user.password} for user in User.objects.all()]
        return Response(usernames)