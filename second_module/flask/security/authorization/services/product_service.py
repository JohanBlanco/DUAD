from datetime import date
from repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_all(self) -> list[dict]:
        products = self.product_repository.get_all()
        return [p.to_dict() for p in products]

    def get_by_id(self, id: int) -> dict | None:
        product = self.product_repository.get_by_id(id)
        return product.to_dict() if product else None

    def create(
        self,
        name: str,
        price: float,
        entry_date: date,
        quantity: int,
    ) -> dict:
        product = self.product_repository.create(
            name=name,
            price=price,
            entry_date=entry_date,
            quantity=quantity,
        )
        return product.to_dict()

    def update(self, id: int, **fields) -> dict | None:
        updated = self.product_repository.update(id, **fields)
        return updated.to_dict() if updated else None

    def delete(self, id: int) -> bool:
        product = self.product_repository.get_by_id(id)
        if not product:
            return False
        self.product_repository.delete(product)
        return True
