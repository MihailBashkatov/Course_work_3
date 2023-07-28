import pytest
from data.filedata import FILEDATA_TESTS
from src.utils import *


@pytest.fixture
def final_result():
    """ Returning final 5 results, using test json file """

    base_data = load_file(FILEDATA_TESTS)
    dict_formatted = dict_consistency(base_data)
    gen_objects = objects_file(dict_formatted)
    base_date = action_date(gen_objects)
    order_date = order_actions_date(base_date)
    order_object_by_date = order_actions_objets(order_date, base_date)
    return get_executed(order_object_by_date)
