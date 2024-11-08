from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données depuis JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Fonction pour lire les données depuis CSV
def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, KeyError):
        pass
    return products

# Fonction pour lire les données depuis SQLite
def read_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
    except sqlite3.Error:
        pass
    finally:
        conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sqlite()
    else:
        return render_template('product_display.html', error_message="Wrong source")

    if product_id is not None:
        products = [p for p in products if p.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)