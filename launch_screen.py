from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSize

class DISPLAY:
    WIDTH = 1920
    HEIGHT = 1080

APP = QApplication([])

MAIN_WINDOW = QWidget()
MAIN_WINDOW.setWindowTitle("Launching...")
MAIN_WINDOW.setFixedSize(QSize(DISPLAY.WIDTH, DISPLAY.HEIGHT))