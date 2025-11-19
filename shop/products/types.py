from typing import TypedDict, List


class Product(TypedDict):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]


ProductList = List[Product]


CategoryList = List[str]
