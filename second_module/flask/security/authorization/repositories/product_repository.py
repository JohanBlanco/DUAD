from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.product_model import Product


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        stmt = select(Product)
        return self.session.scalars(stmt).all()

    def get_by_id(self, id: int):
        return self.session.get(Product, id)

    def get_by_name (self, name: str) -> Product | None | bool:
        stmt = select(Product).where(Product.name == name)
        product = self.session.scalar(stmt)
        return product if product else None

    def create(
        self,
        name: str,
        price: float,
        entry_date: date,
        quantity: int = 0,
    ) -> Product:
        product = Product(
            name=name,
            price=price,
            entry_date=entry_date,
            quantity=quantity,
        )
        self.session.add(product)
        return product

    def update(self, id: int, **fields) -> Product | None:
        product = self.session.get(Product, id)
        if not product:
            return None

        for key, value in fields.items():
            setattr(product, key, value)

        return product

    def delete(self, product: Product):
        self.session.delete(product)
