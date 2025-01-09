

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

    def to_representation(self, instance):
        # 先執行原來的 to_representation 邏輯
        representation = super().to_representation(instance)

        # 加入 price 和 shop_id
        representation['price'] = float(
            instance.price) if instance.price else None
        representation['shop_id'] = str(
            instance.shop_id) if instance.shop_id else None
        representation['id'] = instance.pk

        return representation
