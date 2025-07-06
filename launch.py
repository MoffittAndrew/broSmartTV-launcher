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
LAUNCH_FRAME = QWidget()
LAUNCH_FRAME.setWindowTitle("Launching...")
LAUNCH_FRAME.setFixedSize(QSize(WIDTH, HEIGHT))

# Set background color
LAUNCH_FRAME.setAutoFillBackground(True)
p = LAUNCH_FRAME.palette()
p.setColor(LAUNCH_FRAME.backgroundRole(), Qt.black)
LAUNCH_FRAME.setPalette(p)

# Hide mouse pointer
LAUNCH_FRAME.setCursor(Qt.CursorShape.BlankCursor)
LAUNCH_FRAME.unsetCursor()

async def update():
    
    print("Running update script...")
    await asyncio.sleep(3)
    proc = await asyncio.create_subprocess_exec("update")
    await proc.communicate()
    print("Finished running update script.")
    APP.exit()

def main():
    with qtinter.using_asyncio_from_qt():
        waiting_circ = QtWaitingSpinner()
        waiting_circ.setParent(LAUNCH_FRAME)
        LAUNCH_FRAME.show()
        LAUNCH_FRAME.setCursor(Qt.CursorShape.BlankCursor)
        LAUNCH_FRAME.unsetCursor()
        waiting_circ.start()
        asyncio.create_task(update())
        APP.exec_()

main()