***XPATH FUNCTION***


##from lxml import html
##import requests
##
##
##page = requests.get ('http://harrypotter.wikia.com/wiki/Category:Individuals')
##tree = html.fromstring(page.text)
##
##names = tree.xpath('//li[@title='']/text()')
##dates = tree.xpath('//li[@title='']/text()')
##
##print('names', names)
##print('dates', dates)


def Harry_Potter_Individuals(names):

    root_url = ('http://harrypotter.wikia.com/wiki/Category:Individuals')
    import requests 
    Individuals= requests.get ("http://harrypotter.wikia.com/wiki/Category:Individuals")
    if Individuals.status_code != 200:

        print('Indiviuals')
        return
    
def Harry_Potter_Individuals (names):

    print ("Names", names)
    return

root_url = ('http://harrypotter.wikia.com/wiki/Category:Individuals')
import requests 
Individuals= requests.get ("http://harrypotter.wikia.com/wiki/Category:Individuals")



