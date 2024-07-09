import requests
import pathlib
from pathlib import Path
from bs4 import BeautifulSoup
import requests
import re


url1 = "https://www.oagkenya.go.ke/2021-2022-constituency-development-fund-audit-reports/"
response = requests.get(url1)
content = response.text
soup = BeautifulSoup(content, 'html.parser')
a_tags = soup.find_all('a')

constituencies = [a_tag.get_text(strip=True) for a_tag in a_tags if "NGCDF" in a_tag.get_text()]

url1 = "https://www.oagkenya.go.ke/2021-2022-constituency-development-fund-audit-reports/"
response = requests.get(url1)
content = response.text
soup = BeautifulSoup(content, 'html.parser')


links = soup.find_all('a', class_="dlp-download-link dlp-download-button document-library-pro-button button btn")

link_list = [link['href'] for link in links]

datadir = pathlib.Path("./NGCDF 2021-2022")
datadir.mkdir(parents=True, exist_ok=True)

for link in link_list:
    datadir = pathlib.Path("./NGCDF 2021-2022")
    response = requests.get(link, stream=True)
    for constituency in constituencies:
        if constituency.replace(" ", "-").lower() in link.lower():
            file = datadir / f"{constituency}.pdf"
            with open(file, "wb") as f:
                f.write(response.content)
            break  # Exit the inner loop once a match is found

print("Files downloaded successfully.")
