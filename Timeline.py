import json, os
##
##{
##    "timeline":
##    {
##        "headline":"Hogwarts Students",
##        "type":"default",
##        "text":"<p>Intro body text goes here, blah blah blah</p>",
##        "asset": {
##            "media":"none",
##            "credit":"Grace",
##            "caption":"LIS-697 Fall 2014"
##        },
##        "date": [],
##
##        "era": [
##            {
##                "startDate":"1700,01,01",
##                "endDate":"2014,12,31",
##                "headline":"Headline Goes Here",
##                "text":"<p>Body text goes here, some HTML is OK</p>",
##                "tag":"This is Optional"
##            }
##
##        ]
##    }
##}




data = []

for root, dirs, files in os.walk('.'):
	for file in files:
		if file.endswith('.json'):

			with open(file) as f:
				day = json.loads(f.read())
				print (day)


				# another loop for each headline in day
				for headline in day:

                                        # make a new dictionary for each headline 
                                        dict = {}
                                        dict["startDate"] = birth_year
