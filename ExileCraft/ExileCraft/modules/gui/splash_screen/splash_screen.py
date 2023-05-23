# import main
# from modules.gui.splash_screen.ui_SplashScreen import Ui_SplashScreen
# from qt_core import *
#
# counter = 0
#
#
# class SplashScreen(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_SplashScreen()
#         self.ui.setupUi(self)
#
#         # remove title bar
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         # drop shadow effect
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(20)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 60))
#         self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
#
#         # start qtimer
#         self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.progress)
#         # timer in ms
#         self.timer.start(35)
#
#         # Initial Text
#         self.ui.app_description_label.setText("<strong>WELCOME</strong> TO MY APPLICATION")
#
#         # Change Texts
#         QtCore.QTimer.singleShot(1500, lambda: self.ui.app_description_label.setText("<strong>LOADING</strong> DATABASE"))
#         QtCore.QTimer.singleShot(3000,
#                                  lambda: self.ui.app_description_label.setText("<strong>LOADING</strong> USER INTERFACE"))
#
#         self.show()
#
#     def progress(self):
#
#         global counter
#
#         # set value to progress bar
#         self.ui.progress_bar.setValue(counter)
#
#         # Close Splash Screen and open the app
#         if counter > 100:
#             # Stop Timer
#             self.timer.stop()
#             # Show main window
#             self.main = main.MainWindow()
#             self.main.show()
#
#             self.close()
#
#         counter += 1
