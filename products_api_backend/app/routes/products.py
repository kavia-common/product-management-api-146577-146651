from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError
from ..db import db
from ..models import Product
from ..schemas import ProductCreateSchema, ProductSchema, ProductUpdateSchema

# Blueprint configuration aligned with "Ocean Professional" theme naming and clean organization.
blp = Blueprint(
    "Products",
    "products",
    url_prefix="/products",
    description="Endpoints for managing products (CRUD) with SQLite persistence.",
)


@blp.route("")
class ProductsList(MethodView):
    """
    PUBLIC_INTERFACE
    get:
        List all products.
    post:
        Create a new product.
    """

    @blp.response(HTTPStatus.OK, ProductSchema(many=True))
    @blp.doc(summary="List products", description="Retrieve all products.")
    def get(self):
        """Return all products."""
        products = Product.query.order_by(Product.id.asc()).all()
        return products

    @blp.arguments(ProductCreateSchema)
    @blp.response(HTTPStatus.CREATED, ProductSchema)
    @blp.doc(
        summary="Create product",
        description="Create a new product with name, price, and quantity.",
    )
    def post(self, new_data):
        """
        Create a product.
        """
        try:
            product = Product(
                name=new_data["name"].strip(),
                price=float(new_data["price"]),
                quantity=int(new_data["quantity"]),
            )
            db.session.add(product)
            db.session.commit()
            return product
        except IntegrityError:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message="Integrity error while creating product.")


@blp.route("/<int:product_id>")
class ProductDetail(MethodView):
    """
    PUBLIC_INTERFACE
    get:
        Retrieve a product by id.
    put:
        Update a product by id.
    delete:
        Delete a product by id.
    """

    @blp.response(HTTPStatus.OK, ProductSchema)
    @blp.doc(summary="Get product", description="Retrieve a product by its id.")
    def get(self, product_id: int):
        """Return a single product by id."""
        product = Product.query.get(product_id)
        if not product:
            abort(HTTPStatus.NOT_FOUND, message="Product not found.")
        return product

    @blp.arguments(ProductUpdateSchema)
    @blp.response(HTTPStatus.OK, ProductSchema)
    @blp.doc(
        summary="Update product",
        description="Update fields of a product by id. Supports partial updates.",
    )
    def put(self, update_data, product_id: int):
        """Update an existing product."""
        product = Product.query.get(product_id)
        if not product:
            abort(HTTPStatus.NOT_FOUND, message="Product not found.")

        # Apply partial updates if present
        if "name" in update_data:
            product.name = update_data["name"].strip()
        if "price" in update_data:
            product.price = float(update_data["price"])
        if "quantity" in update_data:
            product.quantity = int(update_data["quantity"])

        try:
            db.session.commit()
            return product
        except IntegrityError:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message="Integrity error while updating product.")

    @blp.response(HTTPStatus.NO_CONTENT)
    @blp.doc(summary="Delete product", description="Delete a product by id.")
    def delete(self, product_id: int):
        """Delete a product by id."""
        product = Product.query.get(product_id)
        if not product:
            abort(HTTPStatus.NOT_FOUND, message="Product not found.")
        db.session.delete(product)
        db.session.commit()
        return ""
