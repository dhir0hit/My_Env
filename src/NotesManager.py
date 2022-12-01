from src.Account import Account


class NotesManager:
    def __init__(self):
        self.AllNotes = []
        # Loading data from database
        self._load_data_()

    def _load_data_(self):
        # open database and load data
        pass


    def new_notes(self, account):
        """
        creates a new Notes in database
        :param account: takes notes class as input
        """
        self.AllNotes.append(account)
        print(self.AllNotes)
        # saving to database

    def get_notes_by_id(self, _uuid):
        """
        gets Notes from list by id
        :param _uuid: takes uuid as input
        :return: Notes as Notes() class
        """
