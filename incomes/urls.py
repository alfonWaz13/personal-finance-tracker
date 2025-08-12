from django.urls import path

from . import views

urlpatterns = [
    path('add_income', views.add_income, name='add_income'),
    path('delete_income/<int:pk>', views.delete_income, name='delete_income'),
]