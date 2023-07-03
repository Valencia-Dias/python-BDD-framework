from utilities.configurations import *


def addBookPayload(isbn,aisle):
    # isbn and aisle should be unique
    body = {
        "name": "Learn Python Automation",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Val Dias"
    }
    return body



def buildPayloadfromDB(query):
    # add the key value pairs here
    # use one row here
    addBody = {}
    tuple1 = getQuery(query)
    addBody['name'] = tuple1[0]
    addBody['isbn'] = tuple1[1]
    addBody['aisle'] = tuple1[2]
    addBody['author'] = tuple1[3]
    return addBody
