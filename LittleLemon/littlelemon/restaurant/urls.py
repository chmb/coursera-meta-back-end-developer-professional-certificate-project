from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemListView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]