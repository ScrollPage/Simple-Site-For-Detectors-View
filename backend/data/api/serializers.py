from rest_framework import serializers 

from data.models import Data

class DataSerializer(serializers.ModelSerializer):
    '''Сериализация данных'''

    class Meta:
        model = Data
        fields = '__all__'