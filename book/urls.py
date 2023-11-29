from django.urls import path
from .views import BookListView, BookFilterView, BookFilterByUser, BookFilterById, Time, CreateBookView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('price', BookFilterView.as_view(), name='price'),
    path('user_price', BookFilterByUser.as_view(), name='user_price'),
    path('user_id', BookFilterById.as_view(), name='user_id'),
    path('time', Time.as_view(), name='time'),
    path('createbook', CreateBookView.as_view(), name = 'createbook')
]
