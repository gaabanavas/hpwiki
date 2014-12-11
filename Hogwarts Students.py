

from bs4 import BeautifulSoup

soup = BeautifulSoup

root_url = 'http://harrypotter.wikia.com/wiki/Category:Hogwarts_students'

import requests
Hogwarts_students = requests.get("http://harrypotter.wikia.com/wiki/Category:Hogwarts_students")
if Hogwarts_students.status_code != 200:


    print ("There was an error with", url)

page_html = Hogwarts_students.text


soup = BeautifulSoup(page_html)

#lets find all the <li> elements because that is where the a links seem to live
all_tr_elements = soup.find_all("tr")


for a_tr in all_tr_elements:

	#print(a_li)

	#now looping through each li, look inside it to see if there is a <a> element
	a_link = a_tr.find("a")

	#if there is
	if a_link != None:


		#we know these links have the "title" attribute so make sure it is there:
		#the element looks like this: <a href="/wiki/Winston%27s_niece" title="Winston's niece">Winston's niece</a>

		if "title"  in a_link.attrs:

			#this is the text inside the a element, so the persons name
			print(a_link.text)

			#and here is the URL to their page
			print ("http://http://harrypotter.wikia.com/" + a_link['href'])

			print ("----")
