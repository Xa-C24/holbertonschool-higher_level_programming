from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données depuis un fichier JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Fonction pour lire les données depuis un fichier CSV
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
def read_sqlite(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (product_id,))
        else:
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
    # Récupérer les paramètres source et id de la requête
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Charger les produits en fonction de la source
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sqlite(product_id)
    else:
        return render_template('product_display.html', error_message="Wrong source. Please use 'json', 'csv', or 'sql'.")

    # Filtrer par ID si un ID est fourni et la source est JSON ou CSV
    if product_id and source in ['json', 'csv']:
        products = [p for p in products if p.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
