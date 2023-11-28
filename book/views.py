from rest_framework.views import APIView
from book.models import BookModel
from .serializer import BookListSerializer, PriceListSerializer
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime, time

class BookListView(APIView):

    def get(self, request):
        book_list = BookModel.objects.all()
        serializer = BookListSerializer(book_list, many=True)
        return Response(serializer.data)


class BookFilterView(APIView):

    def get(self, request):
        # price_filter = BookModel.objects.filter(Q(price = 500) | Q(price = 200))
        price_filter = BookModel.objects.filter(price = 500)
        serializer = PriceListSerializer(price_filter, many=True)
        return Response(serializer.data)


class BookFilterByUser(APIView):

    def user_price_validation(self, user_price):
        if user_price:
            return True
        else:
            return False

    def get(self, request):
        user_price = request.data.get('user_price')
        if self.user_price_validation(user_price):
            user_filter_price = BookModel.objects.filter(price = user_price)
            serializer = PriceListSerializer(user_filter_price, many = True)
            return Response(serializer.data)
        else:
            return Response({
                "Message":"There is no data"
            })

class BookFilterById(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        user_filter_id = BookModel.objects.filter(id = user_id)
        serializer = BookListSerializer(user_filter_id, many = True)
        return Response(serializer.data)


class Time(APIView):
    def get(self, request, *args, **kwargs):
        now = datetime.now().time()
        opening_time = time(4, 0) # 4:00 am
        closing_time = time(18, 0) # 6:00 pm
        if opening_time <= now <= closing_time:
            message = "Welcome! to our online Bookshop"
        else:
            message = "Sorry! our Bookshop closed, You can visit business hours(4:00am to 6:00pm). Thank you."
        return Response({"message" : message})