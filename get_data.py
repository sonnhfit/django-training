import requests
import json


url_req = 'https://graph.facebook.com/me?fields=id,name,link&access_token=EAAJedvCotnwBAEfRO6vTNRK1sZByfpQYoYdkDPZBGWE0yTgJfNUDsFjxhGo4DHjctmK6ZANpCXcY8xK2RzHkXBHWfELAITXtGvjiPuRVOlnrJw8jSdnuVe22tMCu6ZAaNMPB7DYr22SuaWaMamsb1eFbPZCIG9cKOyxm3BrjOiVkdIO4ZBQbNiZCz8YsmZAP2nEZD'

r = requests.get(url_req)

# print(r.status_code)
# print(r.text)

a = json.loads(r.text)
print("ten cua minh la: ", a["name"])