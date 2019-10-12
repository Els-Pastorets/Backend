from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/linea/{item_id}")
async def read_item(item_id):
    api_id = 'b6f70443';
    api_key= '8754120bc4e20bc949df9fd773b741e6';
    url='https://api.tmb.cat/v1/transit/'+item_id+'?app_id='+api_id+'&app_key='+api_key
    data=requests.get(url)
    return data.json()
