from django.shortcuts import render
from common.viewset import StandardResponseViewSet
from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ProductViewSet(StandardResponseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
