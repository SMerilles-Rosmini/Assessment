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
    sql = """SELECT Products.product_id, manufacturers.name, Products.image_url 
            FROM Products
            JOIN manufacturers ON manufacturers.manufacturer_id = Products.product_id;"""
    results = query_db(sql)
    return render_template("templates\products.html", results=results)
    # return str(results)

@app.route("/products/Violins")
def product(id):
    # just one product
    sql = """SELECT * FROM Products 
        WHERE Products.product_type = 'Violin';"""
    result = query_db(sql, (id,), True)
    # return render_template("products.html", result=result)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)