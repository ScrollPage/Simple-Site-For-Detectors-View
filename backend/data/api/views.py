from rest_framework.generics import ListAPIView

from data.models import Data
from .serializers import DataSerializer

class DataView(ListAPIView):
    '''Список данных'''
    serializer_class = DataSerializer
    queryset = Data.objects.all()