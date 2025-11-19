from django.http import HttpRequest
from django.shortcuts import render
import requests

from .services import ProductsService


def categories_page(request: HttpRequest):
    service = ProductsService()
    categories = service.get_categories()

    context = {
        "categories": categories,
    }
    return render(request, "categories/categories.html", context)


def products_list(request: HttpRequest):
    service = ProductsService()
    categories = service.get_categories()
    products = service.get_all_products()

    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, "products/product_list.html", context)


def product_detail(request: HttpRequest, product_id: int):
    service = ProductsService()
    try:
        product = service.get_product_by_id(product_id)
    except requests.HTTPError:
        # можна зробити окрему 404-сторінку
        return render(request, "products/product_not_found.html", status=404)

    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)


def products_by_category(request: HttpRequest, category: str):
    service = ProductsService()
    try:
        products = service.get_products_by_category(category)
    except requests.HTTPError:
        return render(
            request,
            "products/category_not_found.html",
            {"category": category},
            status=404,
        )

    context = {
        "products": products,
        "category": category,
    }
    return render(request, "products/product_list_by_category.html", context)
