
def test_get_operation_amount(final_result):
    for user in final_result:
        assert '.' in user.get_operation_amount()
        assert user.get_operation_amount()[0].isdigit() == True
        assert type(user.get_operation_amount()) == str


def test_get_currency(final_result):
    for user in final_result:
        assert type(user.get_currency()) == str
        assert user.get_currency()[0].isalpha() == True


def test_get_from(final_result):
    for user in final_result:
        assert type(user.get_from()) == str


def test_get_to(final_result):
    for user in final_result:
        assert type(user.get_to()) == str
        assert user.get_to()[-4:-1].isdigit() == True
        assert user.get_to()[-6:-4] == '*' * 2
