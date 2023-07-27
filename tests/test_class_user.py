from data.filedata import FILEDATA
from src.utils import *


base_data = load_file(FILEDATA)
dict_formatted = dict_consistency(base_data)
gen_objects = objects_file(dict_formatted)
base_date = action_date(gen_objects)
order_date = order_actions_date(base_date)
order_object_by_date = order_actions_objets(order_date, base_date)
final_result = get_executed(order_object_by_date)


def test_get_operation_amount():

    for user in final_result:
        assert '.' in user.get_operation_amount()
        assert user.get_operation_amount()[0].isdigit() == True
        assert type(user.get_operation_amount()) == str


def test_get_currency():
    final_result = get_executed(order_object_by_date)
    for user in final_result:
        assert type(user.get_currency()) == str
        assert user.get_currency()[0].isalpha() == True


def test_get_from():
    final_result = get_executed(order_object_by_date)
    for user in final_result:
        assert type(user.get_from()) == str


def test_get_to():
    final_result = get_executed(order_object_by_date)
    for user in final_result:
        assert type(user.get_to()) == str
        assert user.get_to()[-4:-1].isdigit() == True
        assert user.get_to()[-6:-4] == '*' * 2

