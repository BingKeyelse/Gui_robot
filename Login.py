# pyuic5 -x loggui_complete.ui -o loggui_complete.py
# pyuic5 -x main.ui -o ui_main.py  
# pyuic5 -x splash_screen.ui -o ui_splash_screen.py 
# pyuic5 -x Sum_gui.ui -o Sum_gui.py 
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from loggui_complete import Ui_Log_screen
from qtwidgets import PasswordEdit

class Log_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_Log_screen()
        self.uic.setupUi(self)
        self.uic.button_cancer.clicked.connect(self.close)
        self.uic.button_login.clicked.connect(self.login)
        self.uic.button_show.clicked.connect(self.showpass)
        self.uic.button_pass.clicked.connect(self.hidepass)
        self.uic.button_pass.hide()

    def login(self):
        ID = self.uic.screen_user.text()
        password = self.uic.screen_pass.text()
        if ID=="MAGICIAN" and password=='12345':
            print("1")
            self.close()
        else:
            print('error')
    
    def showpass(self):
        self.uic.screen_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uic.button_show.hide()
        self.uic.button_pass.show()
    def hidepass(self):
        self.uic.screen_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uic.button_show.show()
        self.uic.button_pass.hide()

        
if __name__ == "__main__":
    # run app
    # app = QApplication(sys.argv)
    # main_win = Log_screen()
    # main_win.show()
    # sys.exit(app.exec())
    app = QApplication(sys.argv)
    window = Log_screen()
    window.show()
    sys.exit(app.exec_())
