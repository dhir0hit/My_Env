
class PasswordManager:
    def __init__(self):
        self._load_data_()
        self.AccessPass = 0
        self.TotalAccounts = 69
        self.FavoriteAccounts = 0
        self.Unlocked = False
        self.FavoriteAccounts = []
        self.AllAccounts = []

    def _load_data_(self):
        # open database and load data
        pass

    def unlock_manager(self, password):
        return password == "1234"


