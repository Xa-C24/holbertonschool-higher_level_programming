from flask import Flask, render_template, request
import json
import csv

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

@app.route('/display_products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    # Charger les données en fonction de la source
    try:
        if source == 'json':
            products = read_json('products.json')
        elif source == 'csv':
            products = read_csv('products.csv')
        else:
            error = "Wrong source. Please use 'json' or 'csv'."

        # Filtrer par ID si spécifié
        if product_id:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = f"Product with ID {product_id} not found."

    except Exception as e:
        error = f"An error occurred: {str(e)}"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
