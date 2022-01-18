import requests
url=f'https://www.programmableweb.com/api/cdd-vault-rest-api-v1'
r=requests.get(url) #pour recuperer les infos
print(r.text)