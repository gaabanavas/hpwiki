##
##
##
import requests
response = requests.get('http://harrypotter.wikia.com/wiki/Category:Hogwarts_employees' + 'http://harrypotter.wikia.com/wiki/Category:Hogwarts_students')
import bs4
soup = bs4.BeautifulSoup(response.text)
#links = soup.select('li.individuals_names a[href^=/individuals]')
#links = [a.attrs.get('href') for a in soup.select('li.individuals_names a[href^=/individuals]')]

##
##import requests
##import bs4
##index_url = ('http://harrypotter.wikia.com/wiki/Category:Individuals')
##
####def character_names():
####    reponse = request.get('http://harrypotter.wikia.com/wiki/Main_Page')
####    soup = bs4.BeautifulSoup(reponse.text)
####    return [a.attrs.get('href') for a in soup.select('li.character_names a[href^=/individuals')]
##
##def get_character_names(Individual_characters_url):
##    name_data ={}
##    reponse = requests.get('http://harrypotter.wikia.com/wiki/Main_Page' + 'http://harrypotter.wikia.com/wiki/Category:Individuals')
##    soup = bs4.BeautifulSoup(reponse.text)
##    name_data['title'] = [a.get.text() for a in soup.select('div#name a[href^=/class]')
##  
##    
##print(Character_Names())

def printinfo(name, date):
    print ("name", name);
    print ("date", date);
    return
    

##from bs4 import BeautifulSoup
##
##soup = BeautifulSoup
##
##root_url = 'http://harrypotter.wikia.com/wiki/Category:Individuals'
all_li_elements = soup.find_all('li')
for a_li in all_li_elements:

        a_link = a_li.find('a')
        if a_link != None:
            if "title" in a_link.attrs:
                printinfo(a_link.attrs["title"], "date" + a_link['href'])





