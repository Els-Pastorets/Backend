import requests

url='https://api.tmb.cat/v1/transit/parades?app_id=b6f70443&app_key=8754120bc4e20bc949df9fd773b741e6'
data=requests.get(url)

print(data.json())
