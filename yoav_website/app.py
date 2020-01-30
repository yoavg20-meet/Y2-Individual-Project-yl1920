import requests
import json
import random
from flask import Flask, request, redirect, render_template
from flask import session as login_session

from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def home():
    all_products = sorted(query_all(), key=lambda p: p.likes, reverse=True)
    random_chock = random.choice(all_products)
    return render_template('index.html', all_products=all_products, random_chock=random_chock)

@app.route('/product/<product_id>')
def product_page(product_id):
    product = query_by_id(product_id)
    api_url = 'https://api.chucknorris.io/jokes/search?query={}'.format(product.name)
    
    jokes = json.loads(requests.get(api_url).text)['result']
    if jokes:
        joke = random.choice(jokes)['value']
    else:
        joke = "Even Chuck Norris Couldn't find a joke for this chocko."

    return render_template('product_page.html', product=product, joke=joke)

@app.route('/like/<product_id>')
def like_product(product_id):
    add_like(product_id)
    return 'Liked'




    
if __name__=='__main__':
    app.run(debug=True)
