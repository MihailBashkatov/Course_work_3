class User:
    def __init__(self, id_, state, date, operationamount, description, from_, to):
        self.id = id_
        self.state = state
        self.date = date
        self.operationamount = operationamount
        self.description = description
        self.from_ = from_
        self.to = to

    def get_operation_amount(self):
        """Return transferred sum"""
        return self.operationamount['amount']

    def get_currency(self):
        """Return currency"""
        return self.operationamount['currency']['name']

    def get_from(self):
        """ Return string with info about source transfer sum"""

        # Creating 2 arrays. 1 is for wording and another for digits
        list_from = self.from_.split(' ')
        needed_number_str = ''
        wording = ''
        for element in list_from:
            if element.isdigit():
                needed_number_str += element
            else:
                wording += ' ' + element

        # Split digits for 3 blocks
        needed_number_digits = list(needed_number_str)
        list_first = needed_number_digits[0:6]
        list_third = needed_number_digits[-4:]
        list_hide = needed_number_digits[6:-4]

        # The middle block is replacing all values to 'X'
        for i in range(len(list_hide)):
            list_hide[i] = 'X'
        final_list = list_first + list_hide + list_third

        # Joining array with wording anb modified array with digits
        final_string = ''.join(final_list)

        # Splitting final string with ' ', interval 4
        needed_string = ' '.join(list(map(''.join, zip(*[iter(final_string)]*4))))
        return wording.strip() + ' ' + needed_string

    def get_to(self):
        """ Return string with info about destination transfer"""

        # Creating array to filter values for wording
        list_to = list(self.to)
        first_element = ''
        for element in list_to:
            if element.isalpha():
                first_element += element

        # Substituting last 4 digits to '*'
        for i in range((len(list_to)) - 4):
            list_to[i] = '*'
        final_string = ''.join(list_to)
        return first_element + ' ' + final_string[-6:]

    def __repr__(self):
        """ Return final message, depending source transfer"""
        if self.from_ == '':
            return f"""\n{self.date}  {self.description}
{self.get_to()}
{self.get_operation_amount()} {self.get_currency()}"""

        else:
            return f"""\n{self.date}  {self.description}
{self.get_from()} -> {self.get_to()}
{self.get_operation_amount()} {self.get_currency()}"""
