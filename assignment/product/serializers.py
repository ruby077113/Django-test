
from rest_framework import serializers

from shop.models import Shop

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # shop_id is a foreign key to Shop model
    shop_id = serializers.SlugRelatedField(slug_field="name",
                                           queryset=Shop.objects.all())
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2)  # 讓 price 仍然顯示為數字

    class Meta:
        model = Product
        fields = ['id', 'stock_pcs', 'price', 'shop_id', 'vip']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # 如果 price 是字串，將它轉換為數字
        if 'price' in representation:
            representation['price'] = float(representation['price'])
        return representation
