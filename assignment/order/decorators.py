from order.models import Order
from product.models import Product
from rest_framework.response import Response
from rest_framework import status
from functools import wraps


def check_vip(func):
    """
    檢查商品VIP條件
    """
    @wraps(func)
    def decorated(self, request, *args, **kwargs):
        # solution 1: 從Product model中取得Product instance
        product_id = request.data.get('product_id')
        user_vip = request.data.get('vip')
        try:
            product = Product.objects.get(id=product_id)
            if product.vip and not user_vip:
                return Response({'message': 'Product for VIP only.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return func(self, request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    return decorated


def check_product_stock(func):
    """
    檢查商品庫存
    """
    @wraps(func)
    def decorated(self, request, *args, **kwargs):
        # 判斷request method 取得product_id
        if (request.method == "POST"):
            product_id = request.data.get('product_id')

        if (request.method == "DELETE" or request.method == "PUT"):
            order_id = kwargs.get('pk')
            try:
                if not order_id:
                    raise Order.DoesNotExist
                order = self.queryset.get(id=order_id)
                product_id = order.product_id
            except Order.DoesNotExist:
                return Response({'message': 'Order not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # solution 1: 從Product model中取得Product instance
        # print("product decorated", product_id)
        try:
            product = Product.objects.get(id=product_id)
            kwargs['stock_refill'] = False
            # 庫存 < 購買數量
            request_qty = request.data.get('qty') or order.qty
            if (request.method != 'DELETE' and product.stock_pcs < request_qty):
                return Response({'message': 'Product out of stock.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            # 刪除訂單且庫存原本為0
            if (request.method == 'DELETE' and product.stock_pcs == 0):
                kwargs['stock_refill'] = True
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        kwargs['product'] = product
        return func(self, request, *args, **kwargs)
    return decorated
