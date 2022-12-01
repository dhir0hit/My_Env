from src.Account import Account
import pymongo

# client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.tgneiwg.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")
managerCollection = client["myenv"]["manager"]

class PasswordManager:
    def __init__(self):

        # access password as String
        self.AccessPass = "1234"
        # total accounts number
        # as int
        self.TotalAccounts = 0
        # if password manager is unlocked
        # as Boolean
        self.Unlocked = False
        # All accounts list
        self.AllAccounts = []
        # Loading data from database
        self._load_data_()

    def _load_data_(self):
        # open database and load data
        for x in managerCollection.find():
            acc = Account(x['user_name'], x['password'], x['platform'], x['website'], x['_id'])
            self.AllAccounts.append(acc)

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
        acc = {"user_name" : account.Username(), "password" : account.Password(), "platform" : account.Platform(), "website" : account.Website(), "_id" : account.Id()}
        managerCollection.insert_one(acc)

        self.AllAccounts.append(acc)
        print(self.AllAccounts)
        # saving to database


    def get_account_by_id(self, _uuid):
        a = managerCollection.find({"_id":_uuid})
        for i in a:
            print(i)
        """
        gets account from list by id
        :param _uuid: takes uuid as input
        :return: account as Account() class
        """

