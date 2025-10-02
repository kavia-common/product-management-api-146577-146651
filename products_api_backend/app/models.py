from datetime import datetime
from .db import db


class Product(db.Model):
    """
    Product SQLAlchemy model representing an item in the store.

    Fields:
        id (int): Primary key.
        name (str): Product name.
        price (float): Product price.
        quantity (int): Available quantity.
        created_at (datetime): Creation timestamp.
        updated_at (datetime): Last update timestamp.
    """
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self) -> str:
        return f"<Product id={self.id} name={self.name!r} price={self.price} quantity={self.quantity}>"
