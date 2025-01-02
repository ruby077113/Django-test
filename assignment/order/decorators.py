from product.models import Product
from rest_framework.response import Response
from rest_framework import status


def check_vip(func):
    def decorated(request, *args, **kwargs):
        product_id = request.data.get('product_id')
        user_vip = request.data.get('vip')

        try:
            product = Product.objects.get(product_id=product_id)
            if product.vip and not user_vip:
                return Response({'message': 'Product for VIP only.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return func(request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    return decorated
