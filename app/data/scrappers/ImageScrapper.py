import requests
from bs4 import BeautifulSoup

class ImageScrapper():
    URL_PYTHON_DOCKERHUB = "https://hub.docker.com/_/python/tags"

    def __init__(self):
        self.url = self.URL_PYTHON_DOCKERHUB

    def _request(self, version):
        print(self.url+f"?page=1&name={version}")
        response = requests.get(self.url+f"?page=1&name={version}")
        return response

    def scrap_specific_python_version(self, version):
        soup = BeautifulSoup(self._request(version).text, 'html.parser')
        print(soup.prettify())
        repo_list = soup.find_all('div', class_='styles-module__item___sFhku')
        images = []
        for i in repo_list:
            test = i.find('div', {"data-testid": "navToImage"}).text.strip()
            print(test)
        return images