import requests
import json
import csv

# Define the URL and query parameters for the second API
url = "https://www.public.cy/category/"
querystring = {
    "s": "fill out with appropriate values",
    "p": "fill out with appropriate values",
    "locale": "fill out with appropriate values"
}

payload = ""
headers = {
    "cookie": "fill out with appropriate values",
    "User-Agent": "fill out with appropriate values"
}

# Make a request to the second API
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

if response.status_code == 200:
    parsed_response = json.loads(response.text)

    # Create a CSV file for the second API data
    with open("saleAssistant/products/public.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        headers = ["Product Name", "Product Details", "Sale Price", "Link"]
        csv_writer.writerow(headers)  # Write headers

        # Extract and save data from the second API
        for product in parsed_response.get("products", []):
            sku = product.get("sku", {})
            input_string = sku.get("displayName")
            opening_parentheses = input_string.find("(")
            closing_parentheses = input_string.find(")")

            if opening_parentheses != -1 and closing_parentheses != -1:
                product_details = input_string[opening_parentheses + 1 : closing_parentheses].strip()

            if opening_parentheses != -1 and closing_parentheses != -1:
                product_name = input_string[:opening_parentheses].strip()

            sale_price = sku.get("priceInfoDto", {}).get("salePrice")

            link = "https://www.public.cy" + sku.get("url")

            print("Product Name:", product_name)
            print("Product Details:", product_details)
            print("Sale Price:", sale_price)
            print("Link:", link)
            print("-" * 50)

            # Write data to the CSV file
            csv_writer.writerow([product_name, product_details, sale_price, link])

    print("Data from the second API has been scraped and saved to public_second.csv")
else:
    print("Failed to fetch data from the second API. Status code:", response.status_code)
