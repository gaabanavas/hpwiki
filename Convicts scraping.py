from bs4 import BeautifulSoup

soup = BeautifulSoup

root_url = 'http://harrypotter.wikia.com/wiki/Category:Azkaban_convicts'

import requests
Azkaban_Convicts = requests.get("http://harrypotter.wikia.com/wiki/Category:Azkaban_convicts")

if Azkaban_Convicts.status_code != 200:    
    print ("There was an error with", url)

page_html = Azkaban_Convicts.text


soup = BeautifulSoup(page_html)

#lets find all the <li> elements because that is where the a links seem to live
all_li_elements = soup.find_all("li")


for a_li in all_li_elements:

	#print(a_li)

	#now looping through each li, look inside it to see if there is a <a> element
	a_link = a_li.find("a")

	#if there is
	if a_link != None:


		#we know these links have the "title" attribute so make sure it is there:
		#the element looks like this: <a href="/wiki/Winston%27s_niece" title="Winston's niece">Winston's niece</a>

		if "title"  in a _link.attrs:

			#this is the text inside the a element, so the persons name
			print(a_link.text)




			#and here is the URL to their page
			print ("http://http://harrypotter.wikia.com/" + a_link['href'])
			print ("----")


	    



