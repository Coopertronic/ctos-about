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
        self.ui.setupUi(self)
        self.ui.textBrowser.append('<h1>About Coopertronic OS</h1>')
        self.ui.textBrowser.append('<h2>Introduction</h2>')
        self.ui.textBrowser.append('Coopertronic OS is designed primarily for myself to use on all my machines. I have included the things I commonly use from day to day. Coopertronic OS is based on ArchLinux and built using the ArchISO package. I like to use the KDE desktop.')
        self.ui.textBrowser.append('<h3>The KDE Desktop</h3>')
        self.ui.textBrowser.append('The desktop is styled with the theme Neon Knights Green. I have added some of my own art to the mix in the way of wallpapers and icons. It should be easy to see and find your way around.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
