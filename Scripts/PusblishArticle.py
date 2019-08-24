import requests
import json
import hashlib

headers = {'Content-type': 'application/json'}
SALT="BSDN"

user_data=dict(
	email="test5@example.com",
	nickname="Sammy"
)
password="example_password"
passwordHash=hashlib.md5("{}{}".format(password,SALT).encode())
user_data["passwordHash"]=str(passwordHash.digest().hex())
#print(passwordHash.digest().hex())

article_data=dict(
	title="Hello, World 5",
	content=r"This is the 5th article of this system\n\nIt has three parts\n\nWith a image markdown url ![Baidu Logo](https://www.baidu.com/img/bd_logo1.png)"
)


r=requests.post("http://127.0.0.1:5000/api/session",headers=headers,data=json.dumps(user_data))
print(r.text)
print(r.status_code)


rjson=r.json()
token=rjson['data']['sessionToken']
userId=rjson['data']['sessionUserId']


r=requests.post("http://127.0.0.1:5000/api/article?token={}".format(token),headers=headers,data=json.dumps(article_data))
print(r.text)
print(r.ok)