from django.db import models

# Create your models here.


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    shop_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self):
        return self.name
