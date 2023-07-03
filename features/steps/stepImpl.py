from behave import *
import requests
from payLoad import *
from utilities.resources import *
from utilities.configurations import *


@given('Book details that need to be added to the library')
def step_impl(context):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload("asruytyv8fd", "13")


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)
    print(context.response.text)


@then('Book has been added')
def step_impl(context):
    response_json = context.response.json()
    context.book_Id = response_json['ID']
    assert response_json['Msg'] == 'successfully added'


@given('Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.auth_token1 = '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'
    context.s = requests.Session()
    context.s.headers.update({'Authorization': f'Bearer {context.auth_token1}'})


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.s.get(ApiResources.githubRepo)


@then('Status code of the response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
