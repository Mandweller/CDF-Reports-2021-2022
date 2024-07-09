# NGCDF 2021-2022 Reports Downloader

This project downloads the NGCDF (National Government Constituencies Development Fund) audit reports for the year 2021-2022 from the [OAG Kenya website](https://www.oagkenya.go.ke/2021-2022-constituency-development-fund-audit-reports/) and saves them locally.

## Requirements

- Python 3.12.1
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries using `pip`:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script to download the reports:
    ```sh
    app.py
    ```

2. The reports will be saved in the `NGCDF 2021-2022` directory.

## Script Explanation

The script performs the following steps:

1. Sends a GET request to the OAG Kenya website to retrieve the HTML content.

2. Parses the HTML content using BeautifulSoup.

3. Extracts all `<a>` tags that contain the word "NGCDF".

4. Extracts the download links for the reports from `<a>` tags with the class `dlp-download-link dlp-download-button document-library-pro-button button btn`.

5. Downloads the reports and saves them in the `NGCDF 2021-2022` directory with appropriate constituency names.
