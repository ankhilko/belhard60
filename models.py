from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP, Boolean, ForeignKey, DECIMAL, CHAR

Base = declarative_base()


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20), nullable=False) # mustn't be empty
    email = Column(VARCHAR(20), nullable=False, unique=True) # mustn't be empty, should be unique
    date_created = Column(TIMESTAMP, default=datetime.now())

    phone_number = Column(CHAR(13), default=False, unique=True)

    pass


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)  # mustn't be empty, should be unique
    is_published = Column(Boolean, default=False)
    pass


class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(20), nullable=False)  # mustn't be empty
    descr = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    is_published = Column(Boolean, default=False)
    category_id = Column(
        Integer,
        ForeignKey(
            'categories.id', ondelete='CASCADE'),
        nullable=False
    )
    pass

    class Order(Base):
        __tablename__: str = 'orders'

        id = Column(Integer, primary_key=True)
        user_id = Column(Integer,
                         ForeignKey('users.id', ondelete='NO ACTION'),
                         nullable=False)  # mustn't be empty
        is_paid = Column(Boolean, default=False)
        pass

    class OrderItem(Base):
        __tablename__: str = 'order_items'

        id = Column(Integer, primary_key=True)
        order_id = Column(Integer,
                         ForeignKey('orders.id', ondelete='CASCADE'),
                         nullable=False)  # mustn't be empty
        product_id = Column(Integer,
                         ForeignKey('products.id', ondelete='CASCADE'),
                         nullable=False)  # mustn't be empty
        pass

# SQLalchamia - not use for importing to database
# SELECT products.title, order_items.product_id, orders.user_id FROM products JOIN order_items ON order_items.product_id = products.id JOIN orders ON order_items.order_id = orders.id;
