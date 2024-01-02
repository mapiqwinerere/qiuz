#this file include code for interface of proggram for quiz with telegram bot(my school project)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup, QThread, Qt, QTimer
import io
import TgBotMapi as l



#bot defenition
tg = l.TgBot('mapi_bot')


timers = {}
opacity = {}
styles = {}

def up_and_down_opacity(obj, css_txt, num, r, g, b):
    opacity[str(num)] = 13
    #timers
    timers['up_'+str(num)] = QTimer()
    timers['up_'+str(num)].setInterval(10)
    timers['up_'+str(num)].timeout.connect(lambda: up(obj, css_txt, num, r, g, b))

    timers['down_'+str(num)] = QTimer()
    timers['down_'+str(num)].setInterval(10)
    timers['down_'+str(num)].timeout.connect(lambda: down(obj, css_txt, num, r, g, b))
    finish_1 = True
    finish_2 = True
    #defs for buts
    def up(obj, css_txt, num, r, g, b):
        global finish_1
        #print(1)
        if opacity[str(num)] >= 30:
            timers['up_'+str(num)].stop()
        elif finish_2 == False:
            pass
        else:
            finish_1 = False
            opacity[str(num)] += 1
            styles[str(num)] = css_txt + f"background-color: rgba({str(r)}, {str(g)}, {str(b)}, {str(opacity[str(num)])})"
            obj.setStyleSheet(styles[str(num)])
            if opacity[str(num)] == 30:
                finish_1 = True
                timers['up_'+str(num)].stop()

    def down(obj, css_txt, num, r, g, b):
        global finish_1
        global finish_2
        if opacity[str(num)] < 13:
            timers['down_'+str(num)].stop()
        elif finish_1 == False:
            pass
        else:
            finish_2 = False
            opacity[str(num)] -= 1
            styles[str(num)] = css_txt + f"background-color: rgba({str(r)}, {str(g)}, {str(b)}, {str(opacity[str(num)])})"
            obj.setStyleSheet(styles[str(num)])
            
            if opacity[str(num)] <= 13:
                finish_2 = True
                timers['down_'+str(num)].stop()
                num += 1
    obj.enterEvent = lambda event: timers['up_'+str(num)].start()
    obj.leaveEvent = lambda event: timers['down_'+str(num)].start()


class AnimationOpenConfigBut(QThread):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui

        self.group_parallel_cb_o = QParallelAnimationGroup()

        self.group_parallel_cb_o.addAnimation(self.ui.animation_config_create_o)
        self.group_parallel_cb_o.addAnimation(self.ui.animation_config_open_o)

    def run(self):
        self.ui.animation_config_but_o.start()
        self.ui.animation_config_but_o.finished.connect(self.animation_finished)

    def animation_finished(self):
        self.ui.config_but.setText('⚙️')

        for i in self.ui.duo_cb:
            i.raise_()
            i.show()
        
        self.group_parallel_cb_o.start()

        self.ui.config_but.clicked.connect(self.ui.func_animation_config_but_close)        

class AnimationCloseConfigBut(QThread):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui

        self.group_b_c = QParallelAnimationGroup()

        self.group_b_c.addAnimation(self.ui.animation_config_create_c)
        self.group_b_c.addAnimation(self.ui.animation_config_open_c)

        self.group_parallel_cb_c = QSequentialAnimationGroup()
        self.group_parallel_cb_c.addAnimation(self.group_b_c)
        self.group_parallel_cb_c.addAnimation(self.ui.animation_config_but_c)

    def run(self): 
        self.group_parallel_cb_c.start()
        self.ui.animation_config_but_c.finished.connect(self.animation_finished)

    def animation_finished(self):
        self.ui.config_but.setText('⚙️')
        self.ui.config_but.raise_()

        for i in self.ui.duo_cb:
            i.hide()

        self.ui.config_but.clicked.connect(self.ui.func_animation_config_but_open)

#create main window
class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        #start settings
        MainWindow.resize(1920, 1080)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.icon = "D:\programming\quiz\logo.png"
        MainWindow.setWindowIcon(QtGui.QIcon(self.icon))


        #create background of window
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bg.setText("")
        self.bg.setLayoutDirection(QtCore.Qt.LeftToRight)

        #inserting an image
        self.bg.setPixmap(QtGui.QPixmap("D:\programming\quiz\ground_new.png"))
    def setupUi(self, MainWinodow):
        #labels
        self.bg_for_button = QtWidgets.QLabel(self.centralwidget)
        self.bg_for_button.move(665, 380)
        self.bg_for_button.resize(720, 250)
        self.bg_for_button.setStyleSheet("background-color: rgba(255, 255, 255, 13);\n"
                                         "border-radius: 35px;\n"
                                         "border: 8px solid white;\n")
        
        self.bg_for_lines = QtWidgets.QLabel(self.centralwidget)
        self.bg_for_lines.move(722, 415)
        self.bg_for_lines.resize(606, 142)
        self.bg_for_lines.setPixmap(QtGui.QPixmap("D:\programming\quiz\ground_lines.png"))
        
        self.bg_for_settings_but = QtWidgets.QLabel(self.centralwidget)
        self.bg_for_settings_but.move(745, 405)
        self.bg_for_settings_but.resize(560, 150)
        self.bg_for_settings_but.setPixmap(QtGui.QPixmap("D:\programming\quiz\ground_settings_but.png"))

        self.first_line = QtWidgets.QLabel(self.centralwidget)
        self.first_line.move(730, 416)
        self.first_line.resize(550, 37)
        self.first_line.setText("kings_of_rus")
        self.first_line.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 600 18pt \"MS Shell Dlg 2\";")

        self.second_line = QtWidgets.QLabel(self.centralwidget)
        self.second_line.move(730, 464)
        self.second_line.resize(550, 37)
        self.second_line.setText("second_world_war")
        self.second_line.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 600 18pt \"MS Shell Dlg 2\";")
        
        self.third_line = QtWidgets.QLabel(self.centralwidget)
        self.third_line.move(730, 512)
        self.third_line.resize(550, 37)
        self.third_line.setText("first_world_war")
        self.third_line.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 600 18pt \"MS Shell Dlg 2\";")
                                                                                                                                                                                                                    
        #buttons
        self.config_but = QtWidgets.QPushButton(self.centralwidget)
        self.config_but.move(1004, 570)
        self.config_but.resize(40, 40)
        self.config_but.setText('▼')
        self.config_but.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
                                      "color: white;\n"
                                      "background-color: rgba(255, 255, 255, 30);\n"
                                      "border-radius: 11;\n"
                                      "border: 3px solid white;\n")  

        self.edit_but = QtWidgets.QPushButton(self.centralwidget)
        self.edit_but.move(745, 405)
        self.edit_but.resize(164, 150)

        self.add_but = QtWidgets.QPushButton(self.centralwidget)
        self.add_but.move(942, 405)
        self.add_but.resize(164, 150)

        self.settings_but = QtWidgets.QPushButton(self.centralwidget)
        self.settings_but.move(1140, 405)
        self.settings_but.resize(164, 150)

        #lists
        self.lines  = [self.first_line, self.second_line, self.third_line]

        self.settings_widgets = [self.bg_for_settings_but, self.edit_but, self.add_but, self.settings_but]
        for i in self.settings_widgets:
            i.hide()

        #ToolTips
        #self.config_but.setToolTip('Открыть меню')
        #self.add_but.setToolTip("Создать новую викторину")
        #self.edit_but.setToolTip("Изменить созданные викторины")
        #self.settings_but.setToolTip("Открыть настройки")
        
        #opacities
        self.opacity_change_menu = 13
        self.opacity_change_list = 13

        #timers
        self.timer_change_menu_up = QTimer()
        self.timer_change_menu_up.setInterval(5)
        self.timer_change_menu_up.timeout.connect(lambda: change_bg_to_menu_1(self))

        self.timer_change_menu_down = QTimer()
        self.timer_change_menu_down.setInterval(5)
        self.timer_change_menu_down.timeout.connect(lambda: change_bg_to_menu_2(self))

        self.timer_change_list_up = QTimer()
        self.timer_change_list_up.setInterval(5)
        self.timer_change_list_up.timeout.connect(lambda: change_bg_to_list_1(self))

        self.timer_change_list_down = QTimer()
        self.timer_change_list_down.setInterval(5)
        self.timer_change_list_down.timeout.connect(lambda: change_bg_to_list_2(self))

        #connects
        self.config_but.clicked.connect(self.timer_change_menu_up.start)


        #defs for buts
        def change_bg_to_menu_1(self):
            if self.opacity_change_menu >= 150:
                self.timer_change_menu_up.stop()

            else:
                self.opacity_change_menu += 1

                self.bg_for_button.setStyleSheet(f"background-color: rgba(255, 255, 255, {self.opacity_change_menu});\n"
                                                  "border-radius: 35px;\n"
                                                  "border: 8px solid white;\n")

                if self.opacity_change_menu == 150:
                    self.config_but.setText("▲")
                    self.timer_change_menu_up.stop()
                    for i in self.lines: 
                        i.hide()
                    self.bg_for_lines.hide()

                    for i in self.settings_widgets:
                        i.show()
                        i.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

                    self.timer_change_menu_down.start()

        def change_bg_to_menu_2(self):
            if self.opacity_change_menu < 50:
                self.timer_change_menu_down.stop()
            
            else:
                self.opacity_change_menu -= 1
                
                self.bg_for_button.setStyleSheet(f"background-color: rgba(255, 255, 255, {self.opacity_change_menu});\n"
                                                  "border-radius: 35px;\n"
                                                  "border: 8px solid white;\n")
                
                if self.opacity_change_menu <= 50:
                    self.timer_change_menu_down.stop()
                    self.config_but.clicked.connect(self.timer_change_list_up.start)

        
        def change_bg_to_list_1(self):
            if self.opacity_change_list >= 150:
                self.timer_change_list_up.stop()

            else:
                self.opacity_change_list += 1

                self.bg_for_button.setStyleSheet(f"background-color: rgba(255, 255, 255, {self.opacity_change_list});\n"
                                                  "border-radius: 35px;\n"
                                                  "border: 8px solid white;\n")

                if self.opacity_change_list == 150:
                    self.config_but.setText("▲")
                    self.timer_change_list_up.stop()
                    for i in self.settings_widgets: 
                        i.hide()
                    self.bg_for_lines.show()

                    for i in self.lines:
                        i.show()

                    self.timer_change_list_down.start()

        def change_bg_to_list_2(self):
            if self.opacity_change_list < 50:
                self.timer_change_list_down.stop()
            
            else:
                self.opacity_change_list -= 1
                
                self.bg_for_button.setStyleSheet(f"background-color: rgba(255, 255, 255, {self.opacity_change_list});\n"
                                                  "border-radius: 35px;\n"
                                                  "border: 8px solid white;\n")
                
                if self.opacity_change_list <= 50:
                    self.timer_change_list_down.stop()

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
    ui = Ui_MainWindow(MainWindow)

    #application of the ui
    ui.setupUi(MainWindow)

    #final settings
    MainWindow.show()
    MainWindow.showFullScreen()

    sys.exit(app.exec_())