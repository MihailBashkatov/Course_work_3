import json
from datetime import datetime
from src.class_user import User


def load_file(filename):
    """ Return json file in py. format"""

    with open(filename, 'r', encoding='UTF8') as file:
        python_file = file.read()
    return json.loads(python_file)


def dict_consistency(database: list) -> list:
    """ Return formatted dicts list, where all dicts have the same keys"""

    new_dict = []
    for element in database:
        if not element.get('id'):
            element['id'] = ''
        if not element.get('state'):
            element['state'] = ''
        if not element.get('date'):
            element['date'] = ''
        if not element.get('operationAmount'):
            element['operationAmount'] = ''
        if not element.get('description'):
            element['description'] = ''
        if not element.get('from'):
            element['from'] = ''
        if not element.get('to'):
            element['to'] = ''
        new_dict.append(element)
    return new_dict


def objects_file(formatted_dict: list) -> list:
    """ Return objects list for class User"""

    objects_list = []
    for element in formatted_dict:
        user_list = User(element['id'], element['state'], element['date'], element['operationAmount'],
                         element['description'], element['from'], element['to'])
        objects_list.append(user_list)
    return objects_list


def action_date(gen_object: list) -> list:
    """ Return formatted dates as yyyy-mm-dd"""

    element_list = []
    for element in gen_object:
        element_date = element.date.split('T')[0].split('-')[::-1]
        new_date = '-'.join(element_date)
        element.date = new_date
        element_list.append(element)
    return element_list


def order_actions_date(base_date: list) -> list:
    """ Return existing dates from objects list with format 'dd-mm-yyyy"""

    new_order = []
    for element in base_date:
        if element.date == '':
            continue
        else:
            new_order.append(element.date)

    sorted(new_order, key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    return new_order


def order_actions_objets(order_date: list, base_date: list) -> list:
    """ Return sorted objects by dates"""

    # Replacing values in array to objects, using date as a match
    for element in base_date:
        for index in range(len(order_date)):
            if element.date == order_date[index]:
                order_date[index] = element

    return order_date


def get_executed(order_object: list) -> list:
    """ Return five last executed operations"""

    base_data = order_object[::-1]
    executed_list = []
    for element in base_data:
        if element.state == 'EXECUTED':
            executed_list.append(element)
    return executed_list[0:5]
