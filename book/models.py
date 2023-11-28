from django.db import models

class BookModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    writer_name = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Book'