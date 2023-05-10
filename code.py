import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
print(soup.title)

text = soup.find_all(text = 'Python')
print("List = ",text)
size = len(text)
print("Count = ",size)
