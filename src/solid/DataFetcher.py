import requests
from bs4 import BeautifulSoup

class DataFetcher():
    
    def __init__(self, url: str):
        self.url = url
        
    def fetch_data(self):
        self.response = requests.get(self.url)

    def get_movies(self):
        soup = BeautifulSoup(self.response.text, 'lxml')
        data = soup.select('td')
        chunks = [data[x:x+5] for x in range(0, len(data), 5)]
        
        return chunks