from django.shortcuts import render
from rest_framework import viewsets

from order.decorators import check_vip
from product.models import Product
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()  # 保存序列化器数据到模型实例
        print(f"Order created: {order.price}, {order.shop_id}")

    # def perform_create(self, serializer):
    #     # 在保存之前可以執行額外的驗證或處理
    #     if serializer.is_valid():
    #         print("Validated Data:", serializer.validated_data)
    #     else:
    #         # 验证失败，输出错误信息
    #         print("Validation Errors:", serializer.errors)

    # @check_vip
    # def create(self, request, *args, **kwargs):
    #     """
    #     檢查商品 VIP 條件並建立訂單
    #     """
    #     product_id = request.data.get("product_id")
    #     print("product_id", product_id)
    #     if (not product_id):
    #         return Response({"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().create(request, *args, **kwargs)
