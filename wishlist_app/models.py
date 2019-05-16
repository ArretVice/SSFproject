from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(verbose_name='Item name', max_length=100)
    price = models.DecimalField(verbose_name='Price (RUB)', decimal_places=2, max_digits=7, validators=[MinValueValidator(0.01)])
    url = models.URLField(verbose_name='Link to buy', max_length=255)
    comment = models.CharField(verbose_name='Comment', max_length=200, blank=True)
    date_added = models.DateTimeField(verbose_name='Date added', auto_now_add=True)

    def __str__(self):
        return self.item_name
