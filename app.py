import sqlite3
from flask import Flask, g, render_template

DATABASE = 'Database.db'

#intialise app
app = Flask(__name__)

def get_db():
    db = getattr(g,'_Database', None)
    if db is None:
        db = g._Database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_Database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/')
def home():
    #home page - ID, manufacturer, image URL
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Accessory'
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)
    # return str(results)

@app.route("/products/")
def products():
    # products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route("/about/")
def about():
    #About Page - Just text about the website
    return render_template("about.html")

@app.route("/individual_products/<int:id>")
def individ_products(id):
    # indivdual products page - ID, manufacturer, image url
    sql = """SELECT * FROM Products 
        JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
        WHERE Products.product_id = ?;"""
    result = query_db(sql,(id,), True)
    return render_template("individ_product.html", individ_products=result)

if __name__ == '__main__':
    app.run(debug=True)