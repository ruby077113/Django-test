

from product.models import Product
from order.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        source='product',  # 模型中的 `product` 字段
        queryset=Product.objects.all()  # 設定取得資料目標&範圍(所有 Product 實例)
    )

    class Meta:
        model = Order
        fields = ['id', 'product_id', 'qty', 'customer_id', 'price', 'shop_id']
        read_only_fields = ['price', 'shop_id']
