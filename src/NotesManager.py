from src.Notes import Notes
import pymongo

# client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.tgneiwg.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")
notesCollection = client["myenv"]["notes"]


class NotesManager:
    def __init__(self):
        self.AllNotes = []
        # Loading data from database
        self._load_data_()

    def _load_data_(self):
        # open database and load data
        for x in notesCollection.find():
            note = Notes(x['heading'], x['body'])
            self.AllNotes.append(note)
        pass

    def new_notes(self, notes):
        """
        creates a new Notes in database
        :param account: takes notes class as input
        """
        note = {"heading" : notes.Heading(), "body" : notes.body()}
        notesCollection.insert_one(note)
        self.AllNotes.append(note)
        print(self.AllNotes)
        # saving to database

    def get_notes_by_id(self, _uuid):
        a = notesCollection.find({"_id": _uuid})
        for i in a:
            print(i)
        """
        gets Notes from list by id
        :param _uuid: takes uuid as input
        :return: Notes as Notes() class
        """
