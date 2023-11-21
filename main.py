import requests
from datetime import datetime, timedelta
import zipfile
import os

# Define the start and end dates
start_date = datetime(2020, 4, 13)
end_date = datetime(2023, 4, 11)

# Define the base URL
base_url = "https://www.sec.gov/files/forms-144-"

# Function to generate date strings in the required format
def generate_date_string(date):
    return date.strftime("%Y-%m-%d")

# Function to download a zip file given a URL
def download_zip_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
        return file_name
    else:
        print(f"Failed to download: {url}")
        return None

# Function to extract and download PDF files from a ZIP file
def extract_and_download_pdfs(zip_file, date_str):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Create a folder with the date
        folder_name = f"extracted_{date_str}"
        os.makedirs(folder_name, exist_ok=True)

        # Extract all files to the folder
        zip_ref.extractall(folder_name)

        # Find and download all PDF files
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_url = os.path.join(root, file)
                    pdf_name = pdf_url.split("/")[-1]
                    with open(pdf_name, "wb") as pdf_file:
                        with open(pdf_url, "rb") as source_pdf:
                            pdf_file.write(source_pdf.read())
                    print(f"Downloaded PDF: {pdf_name}")

# Iterate over the date range and download files
current_date = start_date
while current_date <= end_date:
    date_str = generate_date_string(current_date)
    url = f"{base_url}{date_str}.zip"
    zip_file = download_zip_file(url)
    if zip_file:
        extract_and_download_pdfs(zip_file, date_str)
    current_date += timedelta(days=1)
