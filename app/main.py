from typing import Union
from fastapi import FastAPI

from app.data.scrappers.VersionnerScrapper import VersionnerScrapper
from app.data.scrappers.ImageScrapper import ImageScrapper

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

@app.get("/python/version/all",
    tags=["Python Versions"],
    summary="Get all the python version available",
    description="Get all the python version available")
def python_all_version_scrapper():
    scrapper = VersionnerScrapper()
    return scrapper.scrap_all_version()

@app.get("/python/version/{version}",
    tags=["Python Versions"],
    summary="Get python version matching the version gvien as parameter",
    description="Get python version matching the version gvien as parameter")
def python_all_specific_version(version: Union[str, None] = None):
    scrapper = VersionnerScrapper()
    python_version = scrapper.scrap_all_version()
    filtered_versions = list(filter(lambda v: v['version'] == version, python_version))
    return filtered_versions

@app.get("/python/version/active",
    tags=["Python Versions"],
    summary="Get all the python version support active",
    description="Get all the python version support active")
def python_active_version_scrapper():
    scrapper = VersionnerScrapper()
    return scrapper.scrap_active_version()



# @app.get("/python/images/{version}")
# def python_images_scrapper(version: Union[str, None] = None):
#     scrapper = ImageScrapper()
#     return scrapper.scrap_specific_python_version(version)