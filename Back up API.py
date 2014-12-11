##
##import requests
## 
## 
##r = requests.get("http://www.pratt.edu")
## 
## 
##print("The request code was:",r.status_code)
##
##print("Here is the text of the webpage:",r.text)
\
##import requests
## 
###as per the DPLA website directions its asks us for get a key for working with the API
##anything = requests.post('http://api.dp.la/v2/api_key/gabanava@pratt.edu')
## 
##print("The request code was:",anything.status_code)
## 
##print("The resultvwas:",anything.text)
##
##API key: 0baaae9a32166deabaa49bfdc137e384


##import requests, json
##
##
##
###Ask for a search results for kittens
##r = requests.get('http://api.dp.la/v2/items?q=kittens&api_key=0baaae9a32166deabaa49bfdc137e384')
## 
##print(r.status_code)
## 
##print(r.text)
## 
###trun it into a python dictonary
##
##
## 
##data = json.loads(r.text)
## 
##print(data)
#anything = requests.post('http://api.dp.la/v2/api_key/gabanava@pratt.edu')
#Ask for a search results for kittens API dictionary
#trun it into a python dictonary



import requests, json, re, sys,


timeline={
	"timeline":
	{
		"headline":"Hogwarts Students",
		"type":"default",
		"text":"<p>Intro body text goes here, blah blah blah</p>",
		"asset": {
			"media":"none",
			"credit":"Grace",
			"caption":"LIS-697 Fall 2014"
		},
		"date": [
                    



                        ],

		"era": [
			{
				"startDate":"1700,01,01",
				"endDate":"2014,12,31",
				"headline":"Headline Goes Here",
				"text":"<p>Body text goes here, some HTML is OK</p>",
				"tag":"This is Optional"
			}

		]
	}
}

patn = re.compile(r'[0-9]{4}')
r = requests.get('http://harrypotter.wikia.com/api.php?action=query&list=categorymembers&cmtitle=Category:Hogwarts_students&cmlimit=500&cmnamespace=0&format=json')
 
print(r.status_code)
 
print(r.text)

data = json.loads(r.text)
for an_entry in data["query"]['categorymembers']:

    r = requests.get('http://harrypotter.wikia.com/api/v1/Articles/Details?ids='+ str(an_entry['pageid']) + '&abstract=100&width=200&height=200')
    page_data = json.loads(r.text)
    print(page_data)
    for item in page_data['items']:
##        for number in item:
        abstract = page_data['items'][item]["abstract"]
        title = page_data['items'][item]["title"]
        birth_year = patn.findall(abstract)
        print(birth_year)
        if len(birth_year)>0:
            birth_year = birth_year[0]
        else:
            birth_year = "unknown"
        timeline_item = {"startDate": birth_year, "endDate": birth_year,  "headline": title, "text": abstract, "tag": "Hogwarts", "assest": {"credit": "GraceA", "caption": "none"}}
        timeline["timeline"]["date"].append(timeline_item)
        with open("timeline.json", "w") as outfile:
            json.dump(timeline, outfile, indent=4)
        #sys.exit()
    
        #print(abstract)
