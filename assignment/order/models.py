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
        print("Order save")
        if not self.pk:  # 創建
            if self.product:
                self.price = self.product.price
                self.shop_id = self.product.shop_id
                self.product.stock_pcs -= self.qty
                self.product.save()
        else:  # 更新
            pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        print("Order delete")
        self.product.stock_pcs += self.qty  # 恢復庫存
        self.product.save()
        super().delete(*args, **kwargs)

    def create(self, validated_data):
        print("Order create")
        super().create(validated_data)
        # pass
