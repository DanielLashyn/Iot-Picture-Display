from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import USER_UI
from PyQt5.QtWidgets import QMessageBox
import USR_recv

# Class that creates the main ui window
class MainWindow(QtWidgets.QMainWindow, USER_UI.Ui_Dialog):

    """UI Window class"""

    # Init the object
    def __init__(self):
        """Initialize the window class"""
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.button_status.clicked.connect(self.send_msg)       
    
    # Function for sending the PA message
    def send_msg(self):
        msg = self.pa_text.toPlainText()
        print(msg)
        USR_recv.send_message(msg)

    # Sets the background color of where the image goes
    def setBackgroundColor(self):
        self.label.setStyleSheet("background-color: blue")
        self.label.setPixmap(QtGui.QPixmap())

    # Sets the image to the label
    def set_image(self):
        self.label.setPixmap(QtGui.QPixmap("./img/receive_image.jpg"))
        self.label.setStyleSheet("")    

    # Function that handles the exit opition
    def exit_func(self):
        exit()

# Start of this module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    USR_recv.set_mainWindow(mainWindow)
    sys.exit(app.exec_()) 
