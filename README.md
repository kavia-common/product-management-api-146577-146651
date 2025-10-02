# product-management-api-146577-146651

Products API - Ocean Professional

A Flask REST API that provides CRUD operations for products with fields:
- id (integer), name (string), price (float), quantity (integer)

Tech:
- Flask + flask-smorest (OpenAPI docs)
- SQLite via SQLAlchemy/Flask-SQLAlchemy
- CORS enabled for development

Run (development):
1) cd products_api_backend
2) pip install -r requirements.txt
3) python run.py
4) Visit Swagger UI: http://localhost:3001/docs
5) OpenAPI schema: http://localhost:3001/openapi.json

Endpoints:
- GET    /products            -> list all products
- GET    /products/<id>       -> get a single product
- POST   /products            -> create a product
- PUT    /products/<id>       -> update a product (partial supported)
- DELETE /products/<id>       -> delete a product

Notes:
- Database file created at products_api_backend/products.db (relative to run path).
- This setup is development-friendly; for production, configure environment variables and use a managed DB.