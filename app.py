from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'
app.static_folder = 'static'

# Crafting scissors data
crafting_scissors = [
    {
        'id': 'crafting-scissors-1',
        'name': 'Crafting Scissors 1',
        'description': 'Designed for precision in crafting projects.',
        'image': 'crafting-scissors-1.jpg',
        'price': '$10',
        'guarantee': '1 year',
        'metal': 'Stainless Steel',
        'usage': 'Crafting',
        'weight': '100 grams',
        'specifications': {
            'length': '8 inches',
            'blade_material': 'High Carbon Steel',
            'cutting_capacity': '5 mm',
        }
    },
    {
        'id': 'crafting-scissors-2',
        'name': 'Crafting Scissors 2',
        'description': 'Designed for precision in crafting projects.',
        'image': 'crafting-scissors-2.jpg',
        'price': '$15',
        'guarantee': '2 years',
        'metal': 'Stainless Steel',
        'usage': 'Crafting',
        'weight': '80 grams',
        'specifications': {
            'length': '9 inches',
            'blade_material': 'High Carbon Steel',
            'cutting_capacity': '8 mm',
        }
    },
    # Add other crafting scissors with similar details
]

welding_machines = [
    {
        'id': '200-amps',
        'name': '200 Amps Welding Machine',
        'description': 'Designed for 200 Amps Arc welding machine.',
        'image': '200-amps-welding-machine.jpg',
        'price': '$500',
        'guarantee': '1 year',
        'metal': 'Steel',
        'usage': 'Welding',
        'weight': '50 lbs',
        'specifications': {
            'length': '15 inches',
            'blade_material': 'Fiber',
            'Burning_capacity': '8 mm',
        }
    },
    {
        'id': '400-amps',
        'name': '400 Amps Welding Machine',
        'description': 'Designed for 400 Amps Arc welding machine.',
        'image': '400-amps-welding-machine.jpg',
        'price': '$800',
        'guarantee': '2 years',
        'metal': 'Iron',
        'usage': 'Heavy Welding',
        'weight': '80 lbs',
        'specifications': {
            'length': '30 inches',
            'blade_material': 'Fiber',
            'Burning_capacity': '16 mm',
        }
    },
    # Add more welding machines as needed
]

# Welding rods data
welding_rods = [
    {
        'id': 'welding-rods-1',
        'name': 'BestArc',
        'description': 'BestArc high quality welding rods.',
        'image': 'welding-rods-1.jpg',
        'price': '$20',
        'guarantee': '1 year',
        'metal': 'Steel',
        'usage': 'Welding',
        'weight': '120 grams',
        'specifications': {
            'Coating': 'Chemicals',
            'length': '12 inches',
            'material': 'iron',
        }
    },
    {
        'id': 'welding-rods-2',
        'name': 'SonBond',
        'description': 'SonBond high quality welding rods.',
        'image': 'welding-rods-2.jpg',
        'price': '$20',
        'guarantee': '1 year',
        'metal': 'Steel',
        'usage': 'Welding',
        'weight': '120 grams',
        'specifications': {
            'Coating': 'Chemicals',
            'length': '12 inches',
            'material': 'iron',
        }
    },
    # Add other welding rods with similar details
]

# Measurement tapes data
measurement_tapes = [
    {
        'id': 'measurement-tape-1',
        'name': '3 Meters',
        'description': 'Designed for measurement tape for 3 meter length.',
        'image': 'measurement-tape-1.jpg',
        'price': '$6',
        'guarantee': '1 year',
        'metal': 'Plastic',
        'usage': 'Measuring',
        'weight': '80 grams',
        'specifications': {
            'length': '3 meters',
            'blade_material': 'Iron',
            'measuring_capacity': '3 m',
        }
    },
    {
        'id': 'measurement-tape-2',
        'name': '5 Meters',
        'description': 'Designed for measurement tape for 5 meter length.',
        'image': 'measurement-tape-1.jpg',
        'price': '$10',
        'guarantee': '1 year',
        'metal': 'Plastic',
        'usage': 'Measuring',
        'weight': '150 grams',
        'specifications': {
            'length': '5 meters',
            'blade_material': 'Iron',
            'measuring_capacity': '5 m',
        }
    },
    # Add other measurement tapes with similar details
]

# Combine all product lists
all_products = crafting_scissors + welding_machines + welding_rods + measurement_tapes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search_results/<category>')
def search_results(category):
    products = []

    if category == 'crafting_scissors':
        products = crafting_scissors
    elif category == 'welding_machines':
        products = welding_machines
    elif category == 'welding_rods':
        products = welding_rods
    elif category == 'measurement_tapes':
        products = measurement_tapes

    return render_template('search_results.html', category=category, products=products)


@app.route('/product_detail/<category>/<product_id>')
def product_detail(category, product_id):
    # Find the product with the given ID
    product = next((p for p in all_products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', category=category, product=product)
    else:
        return render_template('product_not_found.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
 
