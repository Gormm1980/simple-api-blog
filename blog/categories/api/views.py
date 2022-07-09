from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from categories.models import Category
from categories.api.serializer import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
