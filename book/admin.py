from django.contrib import admin
from book.models import BookModel

class BookAdmin(admin.ModelAdmin) :
    list_display = (
        "name", 
        "price", 
        "writer_name", 
        "stock"

    )
admin.site.register(BookModel, BookAdmin)