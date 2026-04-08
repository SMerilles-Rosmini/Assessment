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

# Home page

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

@app.route('/home-high-to-low/')
def home_filtered_desc():
    # filter price home page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case')
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-low-to-high/')
def home_filtered_asc():
    # filter price home page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case')
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-a-to-z/')
def home_a_z():
    # filter name home page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case')
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)


@app.route('/home-z-to-a/')
def home_z_a():
    # filter name home page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case')
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-cremona/')
def home_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1 
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-AB/')
def home_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-daddario/')
def home_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-Anton-breton/')
def home_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-core-academy/')
def home_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-bam/')
def home_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND  Products.product_type IN ('Shoulder_rest', 'String', 'Rosin', 'Case');"""
    results = query_db(sql)
    return render_template("home.html", results=results)

@app.route('/home-remove-all-filters/')
def home_remove_all_filters():
    # Should redirect back to the original page
    return redirect(url_for("home"))
  
# Products page

@app.route("/products/")
def products():
    # products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-high-to-low/')
def product_filtered_desc():
    # filter price products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-low-to-high/')
def product_filtered_asc():
    # filter price products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-a-to-z/')
def product_a_z():
    # filter name products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)


@app.route('/product-z-to-a/')
def product_z_a():
    # filter name products page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-cremona/')
def product_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-AB/')
def product_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-daddario/')
def product_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6;"""           
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-Anton-breton/')
def product_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-core-academy/')
def product_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2;"""
    results = query_db(sql)
    return render_template("products.html", results=results)

@app.route('/product-bam/')
def product_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5;"""
    results = query_db(sql)
    return render_template("products.html", results=results)


# About Page
@app.route("/about/")
def about():
    #About Page - Just text about the website
    return render_template("about.html")

# indvidual products page
@app.route("/individual_products/<int:id>")
def individ_products(id):
    # indivdual products page - ID, manufacturer, image url
    sql = """SELECT * FROM Products
        JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
        WHERE Products.product_id = ?;"""
    result = query_db(sql,(id,), True)  
    return render_template("individ_product.html", individ_products=result)

# Cart functions and page
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

# Rosin page
@app.route("/rosin/")
def rosin():
    # Rosin Product page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-high-to-low/')
def rosin_filtered_desc():
    # filter price rosin page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Rosin'
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-low-to-high/')
def rosin_filtered_asc():
    # filter price rosin page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Rosin'
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-a-to-z/')
def rosin_a_z():
    # filter name rosin page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Rosin'
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)


@app.route('/rosin-z-to-a/')
def rosin_z_a():
    # filter name rosin page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Rosin'
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-cremona/')
def rosin_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1
            AND Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-AB/')
def rosin_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-daddario/')
def rosin_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND Products.product_type = 'Rosin';"""           
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-Anton-breton/')
def rosin_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-core-academy/')
def rosin_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

@app.route('/rosin-bam/')
def rosin_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND Products.product_type = 'Rosin';"""
    results = query_db(sql)
    return render_template("rosin.html", results=results)

# Strings page
@app.route("/strings/")
def string():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-high-to-low/')
def strings_filtered_desc():
    # filter price strings page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'String'
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-low-to-high/')
def strings_filtered_asc():
    # filter price strings page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
             WHERE Products.product_type = 'String'
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-a-to-z/')
def strings_a_z():
    # filter name strings page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
             WHERE Products.product_type = 'String'
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("strings.html", results=results)


@app.route('/strings-z-to-a/')
def strings_z_a():
    # filter name strings page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
             WHERE Products.product_type = 'String'
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-cremona/')
def strings_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1
            AND Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-AB/')
def strings_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-daddario/')
def strings_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND Products.product_type = 'String';"""           
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-Anton-breton/')
def strings_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-core-academy/')
def strings_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

@app.route('/strings-bam/')
def strings_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND Products.product_type = 'String';"""
    results = query_db(sql)
    return render_template("strings.html", results=results)

# Cases and Shoulder rests page
@app.route("/cases_and_shoulder_rests/")
def case_and_shoulder_rest():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases-shoulder-rests-high-to-low/')
def cases_shoulder_rests_filtered_desc():
    # filter price cases and shoulder rests page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Case', 'Shoulder_rest')
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases-shoulder-rests-low-to-high/')
def cases_shoulder_rests_filtered_asc():
    # filter price cases adn shoulder rests page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type IN ('Case', 'Shoulder_rest')
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases-shoulder-rest-a-to-z/')
def cases_shoulder_rests_a_z():
    # filter name cases and shoulder rests page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
             WHERE Products.product_type IN ('Case', 'Shoulder_rest')
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)


@app.route('/cases-shoulder-rest-z-to-a/')
def cases_shoulder_rests_z_a():
    # filter name cases adn shoulder rests page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
             WHERE Products.product_type IN ('Case', 'Shoulder_rest')
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-cremona/')
def cases_shoulder_rests_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1
            AND Products.product_type  IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-AB/')
def cases_shoulder_rests_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND Products.product_type  IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-daddario/')
def cases_shoulder_rests_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND Products.product_type IN ('Case', 'Shoulder_rest');"""           
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-Anton-breton/')
def cases_shoulder_rests_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND Products.product_type  IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-core-academy/')
def cases_shoulder_rests_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND Products.product_type  IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

@app.route('/cases_shoulder_rests-bam/')
def cases_shoulder_rests_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND Products.product_type IN ('Case', 'Shoulder_rest');"""
    results = query_db(sql)
    return render_template("case_shoulder_rest.html", results=results)

# Violins page
@app.route("/violins/")
def violin():
    # Strings Product Page
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id            
            WHERE Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-high-to-low/')
def violins_filtered_desc():
    # filter price violins page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Violin'
            ORDER BY Products.price DESC;"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-low-to-high/')
def violins_filtered_asc():
    # filter price violins page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Violin'
            ORDER BY Products.price ASC;"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-a-to-z/')
def violins_a_z():
    # filter name violins page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Violin'
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql)
    return render_template("violins.html", results=results)


@app.route('/violins-z-to-a/')
def violins_z_a():
    # filter name violins page - ID, manufacturer, image url
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type = 'Violin'
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-cremona/')
def violins_cremona():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1
            AND Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-AB/')
def violins_AB():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND Products.product_type  = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-daddario/')
def violins_daddario():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND Products.product_type = 'Violin';"""           
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-Anton-breton/')
def violins_anton_breton():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-core-academy/')
def violins_core_academy():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)

@app.route('/violins-bam/')
def violins_bam():
    # filter by manufacturer
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND Products.product_type = 'Violin';"""
    results = query_db(sql)
    return render_template("violins.html", results=results)


# Search Bar
@app.route('/search', methods=['POST'])
def search():
    # Search Bar functionality + Search results
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%"
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
             FROM Products
             WHERE Products.product_type LIKE ?
             OR Products.product_name LIKE ?
            ORDER BY LENGTH(Products.product_name) DESC;"""
    results = query_db(sql, [search_term, search_term]) 
    return render_template('search.html', results=results, current_search = search_term_raw)


@app.route('/search-high-to-low',  methods=['POST'])
def search_filtered_desc():
    # filter price search page - ID, manufacturer, image url
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%"
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type LIKE ?
             OR Products.product_name LIKE ?
            ORDER BY Products.price DESC;"""
    results = query_db(sql,  [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-low-to-high',  methods=['POST'])
def search_filtered_asc():
    # filter price search page - ID, manufacturer, image url
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%"
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type LIKE ?
             OR Products.product_name LIKE ?
            ORDER BY Products.price ASC;"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-a-to-z',  methods=['POST'])
def search_a_z():
    # filter name search page - ID, manufacturer, image url
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%"
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type LIKE ?
             OR Products.product_name LIKE ?
            ORDER BY Products.product_name ASC;"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)


@app.route('/search-z-to-a',  methods=['POST'])
def search_z_a():
    # filter name search page - ID, manufacturer, image url
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.product_type LIKE ?
            OR Products.product_name LIKE ?
            ORDER BY Products.product_name DESC;"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)


@app.route('/search-cremona', methods=["POST"])
def search_cremona():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 1
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-AB', methods=["POST"])
def search_AB():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 4
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-daddario', methods=["POST"])
def search_daddario():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 6
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""           
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-anton-breton', methods=["POST"])
def search_anton_breton():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 3
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-core-academy', methods=["POST"])
def search_core_academy():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 2
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

@app.route('/search-bam', methods=["POST"])
def search_bam():
    # filter by manufacturer
    search_term_raw = request.form.get('search', '') 
    search_term = f"%{search_term_raw}%" 
    sql = """SELECT Products.product_id, Products.product_name, Products.image_url, Products.price 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.manufacturer_id
            WHERE Products.manufacturer_id = 5
            AND (Products.product_type LIKE ?
            OR Products.product_name LIKE ?);"""
    results = query_db(sql, [search_term, search_term])
    return render_template("search.html", results=results, current_search = search_term_raw)

# Checkout
@app.route("/checkout_submit/")
def checkout_submit():
    # Submit shipping address function
    return redirect(url_for("payment"))

@app.route("/checkout/")
def checkout():
    # Checkout Page
    return render_template('checkout.html')

# Payment
@app.route("/payment/")
def payment():
    # Payment Function
    sql = """
            SELECT Products.product_id, Products.product_name, Products.price, Products.image_url
            FROM cart
            JOIN Products ON cart.product_id = Products.product_id;"""
    result  = query_db(sql)
    total = sum(item[2] for item in result)
    return render_template('payment.html', total=total)

# Thank you page
@app.route("/thank_you/")
def thanks():
    # A Page that says thank you for purchasing
    return render_template("thanks.html")
# Payment submit
@app.route("/payment_submit/")
def payment_submit():
    # Payment submit Function
    return redirect(url_for("thanks"))


if __name__ == '__main__':

    app.run(debug=True)