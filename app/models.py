from .extensions import db



class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    product_description = db.Column(db.String(256))
    price = db.Column(db.Double)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    images = db.relationship("Image", backref='thing', lazy=True)
    brand = db.relationship("Brand", backref='br', lazy=True)
    category = db.relationship("Category", backref='ca', lazy=True)


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer,
                           db.ForeignKey('products.id'),
                           nullable=False)
    image_name = db.Column(db.String(128), nullable=False)



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128), unique=True, nullable=False)


class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(128), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.ForeignKey('roles.id'))

    role = db.relationship("Role", lazy=True)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    # users = db.relationship("User", back_populates="role")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))
    count = db.Column(db.Integer)
    total_price = db.Column(db.Double)

    user = db.relationship("User", lazy=True)
    product = db.relationship("Product", lazy=True)