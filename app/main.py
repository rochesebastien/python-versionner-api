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

from app.data.scrappers.VersionnerScrapper import VersionnerScrapper
from app.controllers.versions import Versions

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
    

@app.get("/python/version/test")
def python_version_scrapper():
    test = Versions()
    return test.getAllVersions()