from marshmallow import Schema, fields, validates, ValidationError


class ProductBaseSchema(Schema):
    """Base schema with common product fields (without id)."""
    name = fields.Str(required=True, description="Product name", validate=lambda s: len(s.strip()) > 0)
    price = fields.Float(required=True, description="Product price (non-negative)")
    quantity = fields.Integer(required=True, description="Available quantity (non-negative)")

    @validates("price")
    def validate_price(self, value: float) -> None:
        if value < 0:
            raise ValidationError("Price must be non-negative.")

    @validates("quantity")
    def validate_quantity(self, value: int) -> None:
        if value < 0:
            raise ValidationError("Quantity must be non-negative.")


class ProductCreateSchema(ProductBaseSchema):
    """Schema for creating a new product."""


class ProductUpdateSchema(Schema):
    """Schema for updating an existing product (partial updates allowed)."""
    name = fields.Str(required=False, description="Product name", validate=lambda s: len(s.strip()) > 0)
    price = fields.Float(required=False, description="Product price (non-negative)")
    quantity = fields.Integer(required=False, description="Available quantity (non-negative)")

    @validates("price")
    def validate_price(self, value: float) -> None:
        if value < 0:
            raise ValidationError("Price must be non-negative.")

    @validates("quantity")
    def validate_quantity(self, value: int) -> None:
        if value < 0:
            raise ValidationError("Quantity must be non-negative.")


class ProductSchema(ProductBaseSchema):
    """Schema for serializing product data including id."""
    id = fields.Integer(required=True, description="Product identifier")
