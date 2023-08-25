from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns =  [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu'),
] + router.urls