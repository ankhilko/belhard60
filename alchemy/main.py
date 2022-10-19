from typing import Optional

from sqlalchemy import create_engine, select, update, delete, or_, and_
# and_ is the same as .where().where
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from setting import DATABASE_URL
from models import Category, Product

# CRUD create recall update delete

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper


class CRUDCategory:

    @staticmethod
    @create_session
    def add(category: Category, session = None) -> Optional[Category]:
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            print('the entry exists already')
            pass
        else:
            session.refresh(category)
            return category

    @staticmethod
    @create_session
    def get(category_id: int, session = None) -> Optional[Category]:
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        return category[0] if category else None

    @staticmethod
    @create_session
    def update(category: Category, session = None) -> bool:
        category: dict = category.__dict__
        del category['_sa_instance_state']
        session.execute(
            update(Category)
            .where(Category.id == category.get('id'))
            .values(**category)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(category_id: int, session = None) -> None:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()


# with Session() as session:
#     categories = session.execute(
#         select(Category)
#         # .where(or_(Category.is_published == True, Category.id < 5))
#         # .where(or_(Category.id.in_([1, 3, 5])))
#         # .where(or_(Category.id.is_([None])))
#         .where(or_(Category.is_published == True))
#         .order_by(Category.name.desc())
#     )


with Session() as session:
    categories = session.execute(
        select(Category, Product)
        .join(Product, Product.category_id == Category.id)
    )


category = CRUDCategory.get(category_id=1)
category.name = 'Food'

category = CRUDCategory.get(category_id=1)
if category:
    print(*category.__dict__)

