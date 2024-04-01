# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setWindowIcon(QtGui.QIcon('assets/about.svg'))
        self.ui.setupUi(self)
        self.ui.textBrowser.append('<h1>Hello World</h1>')
        self.ui.textBrowser.append('This is a quick demo.')
        self.ui.textBrowser.append('This is just text in a browser')
        self.ui.textBrowser.append('A very simple browser')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
