import requests



#declarem la url de la api
url = 'https://api.tmb.cat/v1/transit/linies/bus/109/parades?app_id=b6f70443&app_key=8754120bc4e20bc949df9fd773b741e6'
data = requests.get(url)

#data = json.load(json_obj)

print(data.json())
