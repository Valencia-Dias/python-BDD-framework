# section 3-31-32
import json
from payLoad import *
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from utilities.resources import *
import requests
from utilities.configurations import *

# addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php", json ={
# "name":"Learn Python Automation",
# "isbn":"abv",
# "aisle":"124",
# "author":"Val Dias"
# },
#     headers= {"Content-Type": "application/json"})

# note for understanding : config = getConfig()
url = getConfig()["API"]["endpoint"] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
# addBook_response = requests.post(url, json=addBookPayload("acv"),headers=headers)
addBook_response = requests.post(url, json=buildPayloadfromDB(query),headers=headers)
# note-isbn and aisle should be unique
# print(addBook_response.json())
response_json = addBook_response.json()
book_Id = response_json['ID']
# print(book_Id)

# delete book

response_deleteBook = requests.post(getConfig()["API"]["endpoint"] + ApiResources.deleteBook, json={"ID": book_Id},
                                    headers={"Content-Type": "application/json"})
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
# print(res_json)
assert res_json["msg"] == "book is successfully deleted"

# Authentication w/o session manager
url = "https://api.github.com/user"
auth_token='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'
headers = {'Authorization': f'Bearer {auth_token}'}
github_response = requests.get(url, headers={'Authorization': f'Bearer {auth_token}'})
assert github_response.status_code == 200



#section 6- 37
#you will get this url from https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user
url2 = "https://api.github.com/user/repos"
auth_token1='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'
# headers1 = {'Authorization': f'Bearer {auth_token}'}
github_response1 = requests.get(url, headers={'Authorization': f'Bearer {auth_token1}'})
# print(github_response1.status_code)


#Authentication with session manager
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {auth_token1}'})
# resp = sm.get(url2,headers={'Authorization': f'Bearer {auth_token1}'})
r = s.get(url2)
print(f'Status Code: {r.status_code}, Content: {r.json()}')
