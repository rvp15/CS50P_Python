import requests
from bs4 import BeautifulSoup

def scrap_pages(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the movie entries
            movies = soup.select('td.titleColumn')
            # Extract information for each movie
            print(soup)

urls = ["https://en.wikipedia.org/wiki/Main_Page"]
scrap_pages(urls)
