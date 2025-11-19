from django.urls import path

from .views import (
    categories_page,
    product_detail,
    products_by_category,
    products_list,
)


urlpatterns = [
    path("", products_list, name="products_list"),
    path("categories/", categories_page, name="categories_page"),
    path("products/", products_list),
    path("products/<int:product_id>/", product_detail, name="product_detail"),
    path(
        "products/category/<str:category>/",
        products_by_category,
        name="products_by_category",
    ),
]
