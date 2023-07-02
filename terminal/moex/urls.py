from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),

    path('moex/', views.moex_list),
    path('group_companies/', views.group_companies),

    path('moex/<int:pk>/', views.moex_detail),
]
