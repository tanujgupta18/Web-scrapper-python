import requests
from bs4 import BeautifulSoup

# Define the list of URLs to scrape
urls = [
    'https://en.wikipedia.org/wiki/Web_scraping',
    'https://en.wikipedia.org/wiki/Data_scraping',
    'https://en.wikipedia.org/wiki/Data_extraction'
]

words_to_find = ['Data','Scraping']

# Iterate through the URLs and perform scraping
for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        content = soup.get_text().lower()

        occurrences = [content.count(word.lower()) for word in words_to_find]

        print(f"Occurrences in {url}:")
        for word, count in zip(words_to_find, occurrences):
            print(f"The word '{word}' appeared {count} times.")
        print()
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
