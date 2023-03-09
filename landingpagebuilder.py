import os
import csv
import urllib.request
from jinja2 import Environment, FileSystemLoader

# Set up environment from Great X Courses
env = Environment(loader=FileSystemLoader('templates'))

# Read in product data from CSV file
with open('product_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    products = [row for row in reader]

# Loop through products and create landing pages
for product in products:
    # Set up context for template rendering
    context = {
        'product_name': product['name'],
        'product_description': product['description'],
        'product_image_url': product['image_url'],
        'product_price': product['price'],
        'affiliate_link': product['affiliate_link']
    }
    # Render the landing page template
    template = env.get_template('landing_page_template.html')
    landing_page_html = template.render(context)
    # Save the landing page HTML to a file
    landing_page_filename = f"{product['name']}_landing_page.html"
    with open(landing_page_filename, 'w') as file:
        file.write(landing_page_html)
    # Download the product image and save it to a file
    image_filename = f"{product['name']}_image.jpg"
    urllib.request.urlretrieve(product['image_url'], image_filename)
