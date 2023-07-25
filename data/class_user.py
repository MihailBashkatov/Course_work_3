class User:
    def __init__(self, id, state, date, operationAmount, description, from_, to):
        self.id = id
        self.state = state
        self.date = date
        self.opertionAmount = operationAmount
        self.description = description
        self.from_ = from_
        self.to = to

    def get_operation_amount(self):
        return self.opertionAmount['amount']

    def get_currency(self):
        return self.opertionAmount['currency']['name']

    def code(self):
        return self.opertionAmount['currency']['code']

    def get_from(self):
        list_from = self.from_.split(' ')
        needed_number_str = ''
        wording = ''
        for element in list_from:
            if element.isdigit():
                needed_number_str += element
            else:
                wording += ' ' + element

        needed_number_digits = list(needed_number_str)
        list_first = needed_number_digits[0:6]
        list_third = needed_number_digits[-4:]
        list_hide = needed_number_digits[6:-4]

        for i in range(len(list_hide)):
            list_hide[i] = 'X'
        final_list = list_first + list_hide + list_third
        final_string = ''.join(final_list)
        needed_string = ' '.join(list(map(''.join, zip(*[iter(final_string)]*4))))
        return wording.strip() + ' ' + needed_string

    def get_to(self):
        list_to = list(self.to)
        first_element = ''
        for element in list_to:
            if element.isalpha():
                first_element += element

        for i in range((len(list_to)) -4):
            list_to[i] = '*'
        final_string = ''.join(list_to)
        return first_element + ' ' + final_string[-6:]

    def __repr__(self):
        if self.from_ == '':
            return f"""\n{self.date}  {self.description}
{self.get_to()}
{self.get_operation_amount()} {self.get_currency()}"""

        else:
            return f"""\n{self.date}  {self.description}
{self.get_from()} -> {self.get_to()}
{self.get_operation_amount()} {self.get_currency()}"""
