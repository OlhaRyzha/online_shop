from dataclasses import dataclass
from typing import cast
import requests

from .types import CategoryList, ProductList, Product


@dataclass
class ProductsService:
    API_URL = "https://dummyjson.com"
    PRODUCTS_URL = "products"

    def _request(self, endpoint: str, params: dict | None = None):
        url = f"{self.API_URL}/{endpoint}"
        response = requests.get(url, params=params)
        return response.json()

    def get_categories(self) -> CategoryList:
        data = self._request(f"{self.PRODUCTS_URL}/categories")
        if not isinstance(data, list):
            return cast(CategoryList, [])

        categories: CategoryList = []
        for item in data:
            if isinstance(item, str):
                categories.append(item)
                continue

            if isinstance(item, dict):
                slug = item.get("slug")
                if not isinstance(slug, str):
                    name = item.get("name")
                    if isinstance(name, str):
                        slug = name.strip().lower().replace(" ", "-")
                if isinstance(slug, str) and slug:
                    categories.append(slug)

        return cast(CategoryList, categories)

    def get_all_products(self) -> ProductList:
        data = self._request(self.PRODUCTS_URL, params={"limit": 0})
        return cast(ProductList, data["products"])

    def get_product_by_id(self, product_id: int) -> Product:
        data = self._request(f"{self.PRODUCTS_URL}/{product_id}")
        return cast(Product, data)

    def get_products_by_category(self, category: str) -> ProductList:
        data = self._request(f"{self.PRODUCTS_URL}/category/{category}")
        return cast(ProductList, data["products"])
