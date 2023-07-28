from data.filedata import FILEDATA
from src.utils import *

filename = FILEDATA


def test_load_file():
    """ Asserting if returning list"""

    assert type(load_file(filename)) == list


def test_dict_consistency():
    """ Asserting if returning list and if element of this list
    does have 7 keys/values"""

    data_base = load_file(filename)
    assert type(dict_consistency(data_base)) == list
    for element in dict_consistency(data_base):
        assert len(element) == 7


formatted_dict = dict_consistency(load_file(filename))


def test_objects_file():
    """ Asserting if returning list and if total amount of objects
    equal the total amount of dicts"""

    assert type(objects_file(formatted_dict)) == list
    assert len(objects_file(formatted_dict)) == len(formatted_dict)


gen_object = objects_file(formatted_dict)


def test_action_date():
    """ Asserting if returning list, if data.field
    does have 2 '-' characters. If total length == 10"""

    assert type(action_date(gen_object)) == list
    assert action_date(gen_object)[0].date.count('-') == 2
    assert len(action_date(gen_object)[0].date) == 10


base_date = action_date(gen_object)


def test_order_actions_date():
    """ Asserting if returning list, if 5th element from the end is '-' character"""

    assert type(order_actions_date(base_date)) == list
    for element in order_actions_date(base_date):
        assert element[-5] == '-'


order_date = order_actions_date(base_date)


def test_order_actions_objets():
    """ Asserting if returning list"""

    assert type(order_actions_objets(order_date, base_date)) == list


order_object = order_actions_objets(order_date, base_date)


def test_get_executed():
    """ Asserting if returning list, if list length is equal to 5"""

    assert type(get_executed(order_object)) == list
    assert len(get_executed(order_object)) == 5
