from rest_framework.generics import ListCreateAPIView
from .models import Smartphone
from .serializer import PhoneSerializer

class PhoneListView(ListCreateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = PhoneSerializer