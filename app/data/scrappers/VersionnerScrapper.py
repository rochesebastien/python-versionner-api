import requests
from bs4 import BeautifulSoup


class VersionnerScrapper():
    URL_PYTHON_WEBSITE = "https://www.python.org/downloads/"

    def __init__(self):
        self.url = self.URL_PYTHON_WEBSITE

    def _request(self):
        response = requests.get(self.url)
        return response


    def scrap_all_version(self):
        soup = BeautifulSoup(self._request().text, 'html.parser')
        version_list = soup.find_all('div', class_='download-list-widget')[0].find_all('li')
        versions = []
        for v in version_list:
            number = v.find('span', class_='release-number').text.strip().replace('Python ', '')
            date = v.find('span', class_='release-date').text.strip()
            link = v.find('span', class_='release-download').find('a')['href']

            version_dict = {
                'version': number,
                'release_date': date,
                'download_link': f"https://www.python.org/downloads/{link}"
            }

            versions.append(version_dict)
        
        return versions

    def scrap_active_version(self):
        soup = BeautifulSoup(self._request().text, 'html.parser')
        version_list = soup.find_all('div', class_='active-release-list-widget')[0].find('ol').find_all('li')
        active_version = []
        for v in version_list:
            number = v.find('span', class_='release-version').text.strip()
            status = v.find('span', class_='release-status').text.strip()
            date = v.find('span', class_='release-start').text.strip()
            support_end = v.find('span', class_='release-end').text.strip()

            version_dict = {
                'version': number,
                'status': status,
                'release_date': date,
                'support_end': support_end
            }
            active_version.append(version_dict)

        return active_version