import os
import asyncio
import qtinter

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSize

class DISPLAY:
    WIDTH = 1920
    HEIGHT = 1080

APP = QApplication([])

MAIN_WINDOW = QWidget()
MAIN_WINDOW.setWindowTitle("Launching...")
MAIN_WINDOW.setFixedSize(QSize(DISPLAY.WIDTH, DISPLAY.HEIGHT))

async def update():
    
    print("Running update script...")
    await asyncio.sleep(3)
    os.system("update")
    print("Finished running update script.")

def main():
    with qtinter.using_asyncio_from_qt():
        MAIN_WINDOW.show()
        asyncio.create_task(update())
        APP.exec_()

main()