import sqlite3
from flask import Flask, g, render_template, redirect, url_for, request

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

def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

@app.route('/')
def home():
    #home page - ID, manufacturer, image URL
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case')
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)
  

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

@app.route("/add_to_cart/<int:id>")
def add_cart(id):
    # Add to cart function
    sql = """INSERT INTO cart (product_id) VALUES (?);"""
    execute_db(sql, (id,))    
    return redirect(url_for("cart_view"))

@app.route("/cart/")
def cart_view():
    # Cart page  
    sql = """
            SELECT Products.product_id, Products.product_name, Products.price, Products.image_url
            FROM cart
            JOIN Products ON cart.product_id = Products.product_id;
        """
    result = query_db(sql) 
    total = sum(item[2] for item in result)
    return render_template("cart.html", result=result, total=total)

@app.route("/remove-from-cart/<int:id>")
def remove_from_cart(id):
    # remove from cart function
    sql = """DELETE FROM cart WHERE product_id = (?);"""
    execute_db(sql, (id,))
    return redirect(url_for("cart_view"))

@app.route("/rosin/")
def rosin():
    # Rosin Product page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route("/strings/")
def string():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route("/cases_and_shoulder_rests/")
def case_and_shoulder_rest():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route("/violins/")
def violin():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/search', methods=['POST'])
def search():
    search_term = f"%{request.form.get('search', '')}%"  
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
             FROM Products
             WHERE Products.product_type LIKE ?
             OR Products.product_name LIKE ?
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql, [search_term, search_term]) 
    return render_template('search.html', results=results)

if __name__ == '__main__':

    app.run(debug=True)