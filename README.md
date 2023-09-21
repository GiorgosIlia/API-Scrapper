# API Scraper

This Python script is a web scraper that fetches data from a specified API and stores it in a CSV file. It is designed to extract product information, including product name, details, sale price, and links.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GiorgosIlia/API-Scrapper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd API-Scrapper
   ```

3. Install the required Python libraries from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

This will install the necessary libraries, including `requests` for making HTTP requests and `csv` for handling CSV files.

## Usage

1. Open the `scraper.py` file and fill out the following placeholders with appropriate values:

   - `querystring`: Replace `"fill out with appropriate values"` with the actual query parameters for the API.
   - `headers`: Fill out the `"cookie"` and `"User-Agent"` fields with the appropriate values for your use case.

2. Run the script:

   ```bash
   python scraper.py
   ```

The script will make a request to the specified API, extract product data, and save it to a CSV file named `file.csv`.

## Output

The script will create a CSV file `file.csv` in the project directory, containing the following columns:

- `Product Name`: The name of the product.
- `Product Details`: Additional details about the product.
- `Sale Price`: The sale price of the product.
- `Link`: The link to the product page.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your branch to your fork.
5. Create a pull request to merge your changes into the main repository.

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [Issues](https://github.com/GiorgosIlia/API-Scrapper/issues) page.

Happy scraping!
