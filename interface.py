#this file include code for interface of proggram for quiz with telegram bot
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup, QThread, Qt, QTimer
import io
import TgBotMapi as l



#bot defenition
tg = l.TgBot('mapi_bot')




#create main window
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #start settings
        MainWindow.resize(1920, 1080)

        self.centralwidget = QtWidgets.QWidget(MainWindow)


        #create background of window
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bg.setText("")
        self.bg.setLayoutDirection(QtCore.Qt.LeftToRight)

        #inserting an image
        self.bg.setPixmap(QtGui.QPixmap("D:\programming\quiz\ground.jpg"))

        #settings for windows
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    #renaming
    def retranslateUi(self, MainWindow):
        global translate_

        translate_ = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle( "Mapi quiz")

if __name__ == "__main__":
    #creating
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    #application of the ui
    ui.setupUi(MainWindow)

    #final settings
    MainWindow.show()
    MainWindow.showFullScreen()

    sys.exit(app.exec_())