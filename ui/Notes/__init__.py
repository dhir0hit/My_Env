from _ast import Delete
from typing import Type
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow)
from ui.Notes.ui_landing import Ui_Form as NotesLanding


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

    

class MainWindow(QMainWindow):
    def __init__(self,window):
        super(MainWindow, self).__init__()
        print ("[+] opened Notes Manager Create")

        self.Window = window.Window


    def run (self,notes):

        self.notes_manager_data = notes
        self.notes_manager_data = NotesLanding()
        self.notes_manager_data.setupUi(self.Window.current_app_container)
        self.Window.verticalLayout_7.addWidget(self.notes_manager_data.Form)






