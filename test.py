# import requests
 
# payload = {
#                 'grant_type': 'password',
#                 'username': "company7@neoinvest.ai",
#                 'password': "Mx2018!",
#             }
# headers = {
#                 # Basic_64_encoded_code
#                 'Authorization': f'Basic     ',
#             }
# files = [

#             ]
# url = f"http://0.0.0.0:8000/c/company7/oauth/token/"

          
# r = requests.post(headers=headers, url=url,
#                                 data=payload, files=files)
# print(r.text.encode('utf8'))
# headers = {
#   'Authorization': 'Basic      '
# }
import requests
import  base64

url = "http://0.0.0.0:8000/c/company7/oauth/token/"

payload = {'username': 'company7@.ai',
'password': 'Mx2018!',
'grant_type': 'password'}


id= "    "
api_key  = str(base64.urlsafe_b64encode(id.encode('utf-8')).decode('utf-8'))


headers = {
  'Authorization': f'Basic {api_key}'
}

print(headers)
response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
