# SEC Forms Downloader

## Project Overview

The SEC Forms Downloader is a Python script that automates the download and extraction of SEC Form 144 filings from the U.S. Securities and Exchange Commission (SEC) website. The script allows users to specify a date range, and it downloads the corresponding ZIP files containing the filings. The PDF files from each ZIP file are then extracted and saved.

## Requirements

- Python 3.x
- Requests library

## Setup

1. **Install Dependencies:**
    ```bash
    pip install requests
    ```

2. **Run the Script:**
    ```bash
    python script.py
    ```
    The script will download SEC Form 144 filings within the specified date range.

## Usage

- **Date Range:**
    - Modify the `start_date` and `end_date` variables in the script to set the desired date range.

- **Base URL:**
    - Adjust the `base_url` variable if there are changes to the SEC website's URL structure.

- **Run the Script:**
    - Execute the script to download and extract SEC Form 144 filings.

## Output

- The script creates a folder for each date in the specified range (e.g., `extracted_YYYY-MM-DD`).
- PDF files are extracted and saved within their respective date folders.

## Notes

- Ensure a stable internet connection for downloading files from the SEC website.

- The script is currently configured for SEC Form 144 filings. Modify the script accordingly for different form types.

- This project is designed for educational purposes and should be used responsibly and in compliance with the SEC's terms and conditions.
