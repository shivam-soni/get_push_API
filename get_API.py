import requests
#payload= {'page': 2, 'count': 25}
r= requests.get('http://127.0.0.1:5000//getdetails/https://www.starmind.ai/',headers={'OAuth': 'Secure'})
#req_data = r.json()
print(r.json())
#print(req_data['company_name'])

