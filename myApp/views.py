from rest_framework import generics
from .serializers import ItemDetailSerializer, ItemListSerializer, \
    CategoryDetailSerializer, CategoryListSerializer, \
    ChoiceCategoryListSerializer, ChoiceCategoryDetailSerializer, \
    ChoicesDetailSerializer, ChoicesListSerializer, \
    OrderDetailSerializer, OrderListSerializer, ItemInfoDetailSerializer, \
    ItemInfoListSerializer, IconDetailSerializer, IconListSerializer, \
    ProfileDetailSerializer, ProfileListSerializer

from .models import Item, Category, ChoiceCategory,\
    Choices, Order, ItemInfo, Icon, Profile


class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    queryset = Item.objects.all()


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class ChoiceCategoryCreateView(generics.CreateAPIView):
    serializer_class = ChoiceCategoryDetailSerializer


class ChoiceCategoryListView(generics.ListAPIView):
    serializer_class = ChoiceCategoryListSerializer
    queryset = ChoiceCategory.objects.all()


class ChoiceCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceCategoryDetailSerializer
    queryset = ChoiceCategory.objects.all()


class ChoicesCreateView(generics.CreateAPIView):
    serializer_class = ChoicesDetailSerializer


class ChoicesListView(generics.ListAPIView):
    serializer_class = ChoicesListSerializer
    queryset = Choices.objects.all()


class ChoicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoicesDetailSerializer
    queryset = Choices.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class ItemInfoCreateView(generics.CreateAPIView):
    serializer_class = ItemInfoDetailSerializer


class ItemInfoListView(generics.ListAPIView):
    serializer_class = ItemInfoListSerializer
    queryset = ItemInfo.objects.all()


class ItemInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemInfoDetailSerializer
    queryset = ItemInfo.objects.all()


class IconCreateView(generics.CreateAPIView):
    serializer_class = IconDetailSerializer


class IconListView(generics.ListAPIView):
    serializer_class = IconListSerializer
    queryset = Icon.objects.all()


class IconDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IconDetailSerializer
    queryset = Icon.objects.all()



class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileDetailSerializer


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()
