from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, description, on_sale, img_url):
	product = Product(
		name=name,
		price=price,
		description=description,
		on_sale=on_sale,
		img_url=img_url)
	session.add(product)
	session.commit()

def query_by_id(_id):
	"""
	Find the first student in the database,
	by their id
	"""
	product = session.query(Product).filter_by(
		id=_id).one()
	return product

def query_all():
	"""
	Print all the students in the database.
	"""
	products = session.query(Product).all()
	return products

def delete_product_id(id1):
	session.query(Product).filter_by(
		id=id1).delete()
	session.commit()


def add_like(product_id):
	product = query_by_id(product_id)
	product.likes += 1
	session.commit()