from database import *


# Delete products
all_products = query_all()

for product in all_products:
	delete_product_id(product.id)

# Create products
all_products = [
	{'name':'large', 'price':15, 'description':'Thats alot of nuttela right there', 'on_sale' : True , 'img_url' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS48zslsnAWG-j_wRw0usEJ0yzfvLJetlxP0q_5sorNJl1i5eg6Tg&s'},
	{'name':'small', 'price':6, 'description':'Only if you are after a meal', 'on_sale': False, 'img_url' : 'https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'},
	{'name':'medium', 'price':10, 'description':'its medium', 'on_sale': False, 'img_url' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWxF5dfB2vXqqkwFXGKatdjhTrkmTpnNzbscL9ewW73cr8BYaf&s'},
	{'name':'marshmallow', 'price':13, 'description':'its very sweet', 'on_sale': True, 'img_url' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxi2u2-KMbnsekcTDtw-OqXqIkrzya6Is9vfOrGPvrL7WJXru0&s'},
	{'name':'vegan', 'price':20, 'description':'pls dont', 'on_sale': False, 'img_url' : 'https://i0.wp.com/cdn-prod.medicalnewstoday.com/content/images/articles/323/323694/cucumber-water-with-basil-mint-and-other-herbs-in-jug.jpg?w=1155&h=1541'},
	{'name':'couple', 'price':25, 'description':'so cute', 'on_sale': False, 'img_url' : 'https://i.pinimg.com/originals/7e/b8/71/7eb871bfc98cbfea026ec8d59b3efbe8.jpg'},
	
]

for product in all_products:
	add_product(product['name'], product["price"], product["description"], product["on_sale"], product["img_url"]) 
