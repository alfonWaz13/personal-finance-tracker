from django.urls import path

from . import views

urlpatterns = [
    path('add_expense', views.add_expense, name='add_expense'),
    path('delete_expense/<int:pk>', views.delete_expense, name='delete_expense'),
]