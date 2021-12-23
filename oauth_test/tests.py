from django.test import TestCase

###https://github.com/jazzband/django-oauth-toolkit

import requests

url = "http://localhost:8000/o/token/"

payload = {'username': '',
'password': '',
'grant_type': 'password'}
files = [

]
headers = {
  'Authorization': 'Basic id-client:secret-client',###Basic_64_encoded_code
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

######
import requests

url = "http://localhost:8000/users/"

payload = {'username': '',
'password': '',
'grant_type': 'password'}
files = [

]
headers = {
  'Authorization': 'Bearer token'
}

#### refresh token

url = "http://localhost:8000/o/token/"

payload = {'refresh_token': 'vaule_of_refresh_token',
'': '',
'grant_type': 'refresh_token'}