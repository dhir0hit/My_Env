from src.Account import Account


class PasswordManager:
    def __init__(self):
        # access password as
        # String
        self.AccessPass = "1234"
        # total accounts number
        # as int
        self.TotalAccounts = 0
        # if password manager is unlocked
        # as Boolean
        self.Unlocked = False
        # All accounts list
        self.AllAccounts = [
            Account("username", "password", "platform", "website")
        ]
        # Loading data from database
        self._load_data_()

    def _load_data_(self):
        # open database and load data
        pass

    def unlock_manager(self, password):
        """
        returns true if password is correct
        :param password: user input password
        :return: boolean
        """
        return password == self.AccessPass

    def new_account(self, account):
        """
        creates a new account in database
        :param account: takes account class as input
        """
        self.AllAccounts.append(account)
        print(self.AllAccounts)
        # saving to database

    def get_account_by_id(self, _uuid):
        """
        gets account from list by id
        :param _uuid: takes uuid as input
        :return: account as Account() class
        """
