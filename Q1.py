import requests

def fetch_json(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()  # Convert response to JSON
        return json_data
    else:
        print("Failed to fetch JSON:", response.status_code)
        return None

# Replace 'your_json_file_url' with the actual URL of the JSON file
url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'

data = fetch_json(url)
print(data)

if data:
    # Extract 'products' dictionary from JSON data
    products = data.get('products', {})

    # Sort products based on descending popularity
    sorted_products = sorted(products.values(), key=lambda x: int(x['popularity']), reverse=True)

    # Display data in a presentation format
    print("Title\t\tPrice\tPopularity")
    print("---------------------------------")
    for product in sorted_products:
        print(f"{product['title']}\t${product['price']}\t{product['popularity']}")
else:
    print("Failed to fetch JSON data.")
