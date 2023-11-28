from rest_framework.serializers import ModelSerializer
from .models import BookModel

class BookListSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'name', 'price', 'stock']


class PriceListSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['name', 'price']
