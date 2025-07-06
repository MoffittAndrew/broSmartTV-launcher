import asyncio
import qtinter

# PyQt imports
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QSize
from waiting_spinner import QtWaitingSpinner

class DISPLAY:
    WIDTH = 1920
    HEIGHT = 1080

APP = QApplication([])

MAIN_WINDOW = QWidget()
MAIN_WINDOW.setWindowTitle("Launching...")
MAIN_WINDOW.setFixedSize(QSize(DISPLAY.WIDTH, DISPLAY.HEIGHT))
MAIN_WINDOW.setAutoFillBackground(True)
p = MAIN_WINDOW.palette()
p.setColor(MAIN_WINDOW.backgroundRole(), Qt.black)
MAIN_WINDOW.setPalette(p)

async def update():
    
    print("Running update script...")
    await asyncio.sleep(3)
    await asyncio.create_subprocess_exec("update")

def main():
    with qtinter.using_asyncio_from_qt():
        circ_bar = QtWaitingSpinner(MAIN_WINDOW)
        MAIN_WINDOW.show()
        MAIN_WINDOW.setCursor(Qt.CursorShape.BlankCursor)
        circ_bar.start()
        asyncio.create_task(update())
        APP.exec_()

main()