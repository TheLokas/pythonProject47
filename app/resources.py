from flask_restx import Resource, Namespace
from .models import Product

ns = Namespace("api")


@ns.route("/products")
class ProductAPI(Resource):
    def get(self):
        products = Product.query.all()
        serialized_products = []
        for product in products:
            serialized_products.append({
                'id': product.id,
                'name': product.name,
                'product_description': product.product_description,
                'price': product.price,
                # Добавьте другие поля при необходимости
            })
        return serialized_products