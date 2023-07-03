#section 3-28-30

# When someone gives you the automation task, its their duty to provide the documentation
# which contains the urls, payload, expected response etc
import json
import requests
#third argument of get() can be headers, which is also optonal
#GET http method has no body to communicate with the servers.
response = requests.get("http://216.10.245.166//Library/GetBook.php", params={"AuthorName": "Rahul Shetty"})
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response)
# print(type(dict_response))
# print(dict_response[0]['isbn'])

# The above method is abit lengthy and hence we use .json() which can return a list or a dictonary.
json_response = response.json()
# print(type(json_response))
# print(json_response)
assert response.status_code ==200, "Code not matching"

#monitor headers
# print(response.headers)
assert  response.headers['Content-Type'] == "application/json;charset=UTF-8", "Headers not matching"

#some logical validaton
#retrieve the book details with isbn RGHCC/ A1b
for actual_book in json_response:
    if actual_book['isbn'] == "A1b":
        print(actual_book)
        break # if break is not put than the for loop will keep running and the actual_book will have details of the last one


expectedBook = {'book_name': 'Postman Course', 'isbn': 'A1b', 'aisle': '1'}
assert  actual_book == expectedBook