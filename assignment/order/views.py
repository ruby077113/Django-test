from common.viewset import StandardResponseViewSet
from order.decorators import check_vip, check_product_stock
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.decorators import action
from django.db.models import Sum, F

# Create your views here.


class OrderViewSet(StandardResponseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @check_product_stock
    @check_vip
    def create(self, request, *args, **kwargs):
        # print("create", request.data)
        return super().create(request, *args, **kwargs)

    @check_product_stock
    def destroy(self, request, *args, **kwargs):
        kwargs["results"] = {"stock_refill": kwargs.get('stock_refill')}
        return super().destroy(request, *args,  **kwargs)

    @action(detail=False, methods=['get'])
    def hot_sales_products(self, request):
        # 取得熱銷商品
        count = int(request.query_params.get('count', 10)) or 10
        total_list = Order.objects.values('product_id').annotate(
            total_qty=Sum('qty')).order_by('-total_qty')[:count]

        return super().response(request, data=total_list, status_code=200)

# def perform_create(self, serializer):
#     # 在保存之前可以執行額外的驗證或處理
#     # 庫存處理邏輯會自動在模型的save()中觸發
#     print("perform_create", serializer.validated_data)
#     product = serializer.validated_data['product']
#     qty = serializer.validated_data['qty']
#     product.stock_pcs = product.stock_pcs-qty
#     product.save()
#     serializer.save()

# def perform_update(self, serializer):
#     # 庫存處理邏輯會自動在模型的save()中觸發
#     serializer.save()

# def perform_destroy(self, instance):
#     # 刪除訂單會自動在模型的 delete() 中恢復庫存
#     instance.delete()
