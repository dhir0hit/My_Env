from _ast import Delete
from typing import Type

def create_notes(noteTitle=None):
    ourNote = Type.Note()
    ourNote.title = noteTitle


class Edit:
    pass

def Edit_notes(noteTitle=None):
    ourNote = Edit.Notes()
    ourNote.title= noteTitle
    
def save_notes(noteTitle=None, save=None):
    ourNote = save.Note()
    ourNote.title = noteTitle

def Delete_notes(noteTitle=None):
    ourNote = Delete.Note()
    ourNote.title = noteTitle

def SaveToDatabase():
    pass
    # conn.database =
    
