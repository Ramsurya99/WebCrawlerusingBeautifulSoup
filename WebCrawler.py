from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.pragyan.org/18/home/events').text

soup = BeautifulSoup(source,'lxml')


f = csv.writer(open('symposium.csv' , 'w'))
f.writerow(['Name', 'Link'])

article=soup.find(class_="cluster-events-container")
#print(article.prettify())

summary = article.find_all("a")
print(summary)

#headline = article.h1.a
#print(headline)

sideline = soup.find(id = "social")
sideline.decompose()

for item in summary:
    name = item.contents[0]
    link = 'https://www.pragyan.org' + item.get('href')
    #print(name)
    f.writerow([name, link])




