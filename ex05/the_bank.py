class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, ’value’):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str)
            raise AttributeError("Attribute name must be a str object.")
    

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.accounts = []

    def add(self, new_account: Account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            raise AssertionError("Argument given is not an Account instance")
            return False

        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        self.accounts.append(new_account)
        return True


    def transfer(self, origin: Account, dest: Account, amount: int or float):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float OR INT(amount) amount to transfer
            @return True if success, False if an error occured
        """ 
        if not isinstance(origin, Account) or not isinstance(dest, Account):
            raise AssertionError("Origin and/or dest are/is not an Account instance")
            return False
        if type(amount) is not int or type(amount) is not float:
            raise AssertionError("Amount given is not a number")
            return False

    def fix_account(self, name: str or Account):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if type(name) is not str or not isinstance(name, Account):
            raise AssertionError("Name given is not a string or Account object")
            return False
