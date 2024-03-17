from typing import Union
from fastapi import FastAPI


metadata = {
    "title": "Python Versionner API",
    "description": "API for scrapping python versions and images",
    "version": "1.0.0",
}

app = FastAPI(
     title=metadata["title"],
    description=metadata["description"],
    version=metadata["version"],
)


import requests
from bs4 import BeautifulSoup




@app.get("/")
def read_root():
    return {"Python Versionner API": "Running"}

    
@app.get("/api/status",
    tags=["Status"],
    summary="Get the status of the API",
    description="Get the status of the API")
def status():
    response = {
        'status': 'Ok',
        'message':"API Started !"
        }
    return response

@app.get("/python/version/all")
def python_version_scrapper():

    url = "https://www.python.org/downloads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    version_list = soup.find_all('div', class_='download-list-widget')[0].find_all('li')
    versions = []
    print(type(version_list))
    for v in version_list:
        release_number = v.find('span', class_='release-number').text.strip()
        release_date = v.find('span', class_='release-date').text.strip()
        download_link = v.find('span', class_='release-download').find('a')['href']

        version_dict = {
            'version': release_number,
            'release_date': release_date,
            'download_link': f"https://www.python.org/downloads/{download_link}"
        }

        versions.append(version_dict)
    
    return versions

