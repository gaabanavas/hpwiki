import requests, json
payload = {'sourceResource.subject': 'Names', 'api_key': '0baaae9a32166deabaa49bfdc137e384'}
r = requests.get('http://harrypotter.wikia.com/api/v1/Search/List?query=Black&rank=newest&limit=25&minArticleQuality=10&batch=50&namespaces=0%2C14', params=payload)



print(r.status_code)
 
print(r.text)

data = json.loads(r.text)
 
print(data)
