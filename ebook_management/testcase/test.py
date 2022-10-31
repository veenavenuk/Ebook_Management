import json
import jsonpath
import requests

def test():
	app_URL = 'http://127.0.0.1:8000/ebookapi/register-user/'
	filedata=open('file.json','r')
	request_json = json.loads(filedata.read())
	response=requests.post(app_URL,request_json)
	print(response.text)
	
test()
