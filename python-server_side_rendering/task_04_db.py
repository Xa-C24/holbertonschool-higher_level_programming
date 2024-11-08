from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(product_id=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if product_id:
        cursor.execute("SELECT * FROM Products WHERE id=?", (product_id,))
    else:
        cursor.execute("SELECT * FROM Products")
    
    rows = cursor.fetchall()
    conn.close()
    products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    return products

@app.route('/display_products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    try:
        # Charger les données en fonction de la source
        if source == 'json':
            products = read_json('products.json')
        elif source == 'csv':
            products = read_csv('products.csv')
        elif source == 'sql':
            if product_id:
                products = read_sqlite(int(product_id))
            else:
                products = read_sqlite()
            if not products:
                error = f"Product with ID {product_id} not found."
        else:
            error = "Wrong source. Please use 'json', 'csv', or 'sql'."

    except ValueError:
        error = "Invalid ID format. Please provide a numeric ID."
    except FileNotFoundError:
        error = f"File not found. Please check the source file."
    except sqlite3.DatabaseError:
        error = "An error occurred with the database connection."

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
