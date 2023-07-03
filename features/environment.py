# The code in this file runs before and after some events

import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        response_deleteBook = requests.post(getConfig()["API"]["endpoint"] + ApiResources.deleteBook,
                                            json={"ID": context.book_Id},
                                            headers={"Content-Type": "application/json"})
        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()
        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
