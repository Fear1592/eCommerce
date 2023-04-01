from django.urls import path
from .views import *

urlpatterns = [
    path('item/create/', ItemCreateView.as_view()),
    path('all/', ItemListView.as_view()),
    path('item/detail/<int:pk>/', ItemDetailView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/all/', CategoryListView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view()),
    path('choice-category/create/', ChoiceCategoryCreateView.as_view()),
    path('choice-category/all/', ChoiceCategoryListView.as_view()),
    path('choice-category/detail/<int:pk>/', ChoiceCategoryDetailView.as_view()),
    path('choices/create/', ChoicesCreateView.as_view()),
    path('choices/all/', ChoicesListView.as_view()),
    path('choices/detail/<int:pk>/', ChoicesDetailView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/all/', OrderListView.as_view()),
    path('order/detail/<int:pk>/', OrderDetailView.as_view()),
    path('iteminfo/create/', ItemInfoCreateView.as_view()),
    path('iteminfo/all/', ItemInfoListView.as_view()),
    path('iteminfo/detail/<int:pk>/', ItemInfoDetailView.as_view()),
    path('icon/create/', IconCreateView.as_view()),
    path('icon/all/', IconListView.as_view()),
    path('icon/detail/<int:pk>/', IconDetailView.as_view()),
    path('profile/create/', ProfileCreateView.as_view()),
    path('profile/all/', ProfileListView.as_view()),
    path('profile/detail/<int:pk>/', ProfileDetailView.as_view()),
]
