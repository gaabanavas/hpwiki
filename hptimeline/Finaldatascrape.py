



import requests, json, re, sys


timeline={
	"timeline":
	{
		"headline":"Hogwarts Students",
		"type":"default",
		"text":"<p>Intro body text goes here, blah blah blah</p>",
		"asset": {
			"media":"http://harrypotter.wikia.com/wiki/File.jpg",
                        "thumbnail":"optional-32x32px.jpg",
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
        timeline_item = {"startDate": birth_year, "endDate": birth_year,  "headline": title, "text": abstract, "tag": "Hogwarts", "asset": {"credit": "GraceA", "caption": "none"}}
        timeline["timeline"]["date"].append(timeline_item)
        with open("timeline.json", "w") as outfile:
            json.dump(timeline, outfile, indent=4)
        #sys.exit()
    
        #print(abstract)
