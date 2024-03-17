
import requests
from bs4 import BeautifulSoup


class VersionnerScrapper:

    def __init__(self, url):
        self.url = url

    def _request(self):
        response = requests.get(self.url)
        return response


    def scrap_all_version(self):
        soup = BeautifulSoup(self._request().text, 'html.parser')
        version_list = soup.find_all('div', class_='download-list-widget')[0].find_all('li')
        versions = []
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