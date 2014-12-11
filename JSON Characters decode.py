import json
studentnames = []



data= [{"http://harrypotter.wikia.com/api.php?action=query&list=categorymembers&cmtitle=Category:Hogwarts_students&cmlimit=500&cmnamespace=0&format=json"}]
print('data', data)

##import requests, json
##
##payload = {'sourceResource.subject': 'Students', 'api_key': '0baaae9a32166deabaa49bfdc137e384'}
##r = requests.get('http://harrypotter.wikia.com/api.php?action=query&list=categorymembers&cmtitle=Category:Hogwarts_students&cmlimit=500&cmnamespace=0&format=json', params=payload)
##
##a_character = {"title": "potter, harry" }
##
##studentnames.append(a_character)
##
##with open('API.py', 'w') as f:
##
##    f.write(json.dumps(studentnames, indent=4))

##import requests, json
##payload = {'sourceResource.subject': 'Students', 'api_key': '0baaae9a32166deabaa49bfdc137e384'}
##r = requests.get('http://harrypotter.wikia.com/api.php?action=query&list=categorymembers&cmtitle=Category:Hogwarts_students&cmlimit=500&cmnamespace=0&format=json', params=payload)
##
##with open('students.text', 'w') as outfile:
##    json.dump(data, outfile)
