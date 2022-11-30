from src.Account import Account


class PasswordManager:
    def __init__(self):
        self._load_data_()
        self.AccessPass = 0
        self.TotalAccounts = 69
        self.FavoriteAccounts = 0
        self.Unlocked = False
        self.AllAccounts = []

    def _load_data_(self):
        # open database and load data
        pass

    def unlock_manager(self, password):
        return password == "1234"

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
