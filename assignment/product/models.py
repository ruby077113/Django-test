from django.db import models
from shop.models import Shop


# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    stock_pcs = models.IntegerField(
        default=0, help_text="Enter the number of items in stock.")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_id = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    vip = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Product Information'

    # def __str__(self):
    #     return str(self.id)
