import json

from data.class_user import User


def load_file(filename):
    """ Return json file in py. format"""
    with open(filename, 'r', encoding='UTF8') as file:
       python_file = file.read()
    return json.loads(python_file)


def objects_file():
    objects_list = []
    user = User()
    for user_object in load_file('data/operations.json'):
        if user_object.get("id"):
            user.id = user_object["id"]
        if user_object.get("state"):
            user.state = user_object["state"]
        if user_object.get("operationAmount"):
            user.opertionAmoint = user_object["operationAmount"]
        if user_object.get("date"):
            user.date = user_object["date"]
        if user_object.get("description"):
            user.description = user_object["description"]
        if user_object.get("from"):
            user.fr_ = user_object["from"]
        if user_object.get("to"):
            user.to = user_object["to"]
        objects_list.append(user)
    return objects_list
