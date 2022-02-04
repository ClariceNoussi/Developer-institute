import requests
url=f'https://explorer.natureserve.org/api/data/taxon/ELEMENT_GLOBAL.2.150000'
r=requests.get(url) #pour recuperer les infos
for i in range(150000-155000):
    d = requests.get(f'https://explorer.natureserve.org/api/data/taxon/ELEMENT_GLOBAL.2.{i}')
    print(i)
    print(d.text)
    print('---------------------------------------------------------------')