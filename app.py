from PyQt5 import QtCore, QtGui, QtWidgets
import json

from ui import Ui_MainWindow


class Notewindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}

        self.ui.pushButton.cliked.connect(self.add_not)
        self.ui.listWidget.itemClicked.connect(self.show_note)
        self.ui.pushButton_3.clicked.connect(self.save_note)
        self.ui.pushButton_4.clicked.connect(self.del_note)
        self.ui.pushButton_5.clicked.connect(self.add_tag)
        self.ui.pushButton_6.clicked.connect(self.search_tag)


        # Завантажити заміток
        self.load_notes()

    def load_notes(self):
        try:
            with open('notes_data.json', 'r', encoding='utf-8') as file:
                self.notes = json.load(file)
            self.ui.listWidget.addItems(self.notes)
        except FileNotFoundError:
            self.notes = {}







