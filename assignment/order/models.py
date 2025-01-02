from django.db import models

from product.models import Product

# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)  # order_id
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)  # 商品id 外鍵關聯到 Product 模型
    qty = models.IntegerField()  # 購買數量
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品單價
    shop_id = models.CharField(max_length=100)  # 商品所屬館別
    customer_id = models.IntegerField()  # 購買者id
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間

    class Meta:
        ordering = ['id']
        verbose_name = 'Order Information'

    def save(self, *args, **kwargs):
        if self.product:
            # product = Product.objects.get(id=self.product.id)
            print("product", self.product)
            print("price", self.product.price)
            print("shop_id", self.product.shop_id)
            # self.price = self.product.price
            # self.shop_id = self.product.shop_id
            self.price = 100.00
            self.shop_id = 'um'
        else:
            print("No product found, price and shop_id not set.")
        super().save(*args, **kwargs)
