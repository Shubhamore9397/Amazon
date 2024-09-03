

from django.urls import path
from product import views

urlpatterns = [
    path('',views.home),
    path('view', views.view_product),
    path('add', views.add_product),
    path('delete/<product_id>', views.delete_product),
    path('update/<product_id>', views.update_product),
]
