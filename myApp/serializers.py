from rest_framework import serializers
from .models import Item, Category, ChoiceCategory, \
    Choices, Order, ItemInfo, Icon, Profile


class ItemDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = ('id', 'name', 'price',
                  'discount', 'created_at', 'info_item',
                  'category', 'user', 'choice',
                  'all_icon')


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'price',
                  'discount', 'created_at', 'info_item',
                  'category', 'user', 'choice',
                  'all_icon')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ChoiceCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceCategory
        fields = '__all__'


class ChoiceCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceCategory
        fields = '__all__'


class ChoicesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class ChoicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ItemInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        fields = '__all__'


class ItemInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        fields = '__all__'


class IconDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


class IconListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
