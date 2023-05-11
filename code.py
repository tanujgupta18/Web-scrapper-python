import requests
from bs4 import BeautifulSoup

#Requesting URL
r = requests.get('https://www.geeksforgeeks.org/java/')

# Converting to Html Code 
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

#Exctracting Title of Web Page
print(soup.title)

#Finding Occurence Of a Specific Word in Web Page
text = soup.get_text(strip=True).lower().count('Hello World'.lower())
print("Count = ",text)

