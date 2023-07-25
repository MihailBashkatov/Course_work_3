from data.filedata import FILEDATA
from utils import *


base_data = load_file(FILEDATA)
dict_formatted = dict_consistency(base_data)
gen_objects = objects_file(dict_formatted)
base_date = action_date(gen_objects)
order_date = order_actions_date(base_date)
order_object_by_date = order_actions_objets(order_date, base_date)
final_result = get_executed(order_object_by_date)


print("*" * 45)
for transfer in final_result:
    print(transfer)

