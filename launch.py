import asyncio
import qtinter

# PyQt imports
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QSize
from waiting_spinner import QtWaitingSpinner

WIDTH = 1920
HEIGHT = 1080
APP = QApplication([])

# Initialize window
MAIN_WINDOW = QWidget()
MAIN_WINDOW.setWindowTitle("Launching...")
MAIN_WINDOW.setFixedSize(QSize(WIDTH, HEIGHT))

# Set background color
MAIN_WINDOW.setAutoFillBackground(True)
p = MAIN_WINDOW.palette()
p.setColor(MAIN_WINDOW.backgroundRole(), Qt.black)
MAIN_WINDOW.setPalette(p)

# Hide mouse pointer
MAIN_WINDOW.setCursor(Qt.CursorShape.BlankCursor)
MAIN_WINDOW.unsetCursor()

async def update():
    
    print("Running update script...")
    await asyncio.sleep(3)
    await asyncio.create_subprocess_exec("update")

def main():
    with qtinter.using_asyncio_from_qt():
        waiting_circ = QtWaitingSpinner()
        waiting_circ.setParent(MAIN_WINDOW)
        MAIN_WINDOW.show()
        waiting_circ.start()
        asyncio.create_task(update())
        APP.exec_()

main()