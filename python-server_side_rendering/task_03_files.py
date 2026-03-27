from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    items_list = data.get("items", [])

    return render_template('items.html', items=items_list)

def read_products_from_json(path='products.json'):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def read_products_from_csv(path='products.csv'):
    products = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:

            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products_list = []
    error_message = None  

    if source == 'json':
        products_list = read_products_from_json()
    elif source == 'csv':
        products_list = read_products_from_csv()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html',
                               products=[],
                               error_message=error_message)

    if id_param:
        try:
            wanted_id = int(id_param)
        except ValueError:
            error_message = "Product not found"
            return render_template('product_display.html',
                                   products=[],
                                   error_message=error_message)

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            error_message = "Product not found"
            return render_template('product_display.html',
                                   products=[],
                                   error_message=error_message)
        products_list = filtered

    return render_template('product_display.html',
                           products=products_list,
                           error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
