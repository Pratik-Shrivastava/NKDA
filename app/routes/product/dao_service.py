from typing import List
from app import orm as ORM
from app import db


def add_product(product : dict) -> int | None:
    try:
        product_model = ORM.Product(
            product_name = Product.get('product_name'),
            product_description = Product.get('product_description'),
            product_price = Product.get('product_price')
        )

        db.session.add(product_model)
        db.session.flush([product_model])
    
        db.session.commit()
        return product_model.id
    
    except Exception as e:
        db.session.rollback()
        raise e


def get_product_by_id(id: int) -> ORM.Product | None:
    return ORM.Product.query.filter_by(id=id).first()

def get_product_list() -> List[ORM.Product] | list:
    return ORM.Product.query.all()

def update_product(product: dict) -> bool:
    try:
        product_info = get_product_by_id(product.get('id'))

        if product_info is None:
            return False

        product_info.product_name = product.get('product_name')
        product_info.product_description = product.get('product_description')
        product_info.product_price = product.get('product_price') 
       
        db.session.commit()
        return True

    except Exception as e:
        db.session.rollback()
        raise e

def delete_product(product_id: int) -> bool:
    try:
        product_info = get_product_by_id(product_id)
        
        if product_info is None:
            return False

        db.session.delete(product_info)
        db.session.commit()
        return True
    
    except Exception as e:
        db.session.rollback()
        raise e
 
         