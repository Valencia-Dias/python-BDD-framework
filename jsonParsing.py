#section 3-24-25
import json
courses = '{"name": "Val","lang": ["Java","Python"]}'

# JSON parsing is the process of converting a JSON object in text format to a
# Javascript object that can be used inside a program

#loads()- parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['name'])
# print(dict_courses['lang'][0])
# print(dict_courses['lang'][1])
list_languages = dict_courses['lang']
# print(type(list_languages))



#PARSE CONTENT PRESENT IN JSON FILE
# loads() is for parsing string
# load() is for parsing file and it will later give a dictionary
with open('course.json') as f:
    data = json.load(f)
    # print(data)
    # print(type(data))
    # print(data["courses"])
    # print(data["courses"][1]["title"])
    # print(data["dashboard"]["website"])

#section 3-26

    #price of rpa
    print(data["courses"][2]['price'])
    for course in data["courses"]:
        # print(course)
        if course["title"] =="RPA":
            print(course["price"])
            assert course["price"] == 45


#section 3- 27
#comparing dbDemo.py json files
#so for that covert to dict first and than compare the dictionaries

with open("course1.json") as f2:
    data2 = json.load(f2)
    print(data == data2) # this will return True/False
    assert data == data2