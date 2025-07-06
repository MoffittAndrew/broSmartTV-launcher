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
LAUNCH_FRAME.setContentsMargins(0, 0, 0, 0)

# Set background color
LAUNCH_FRAME.setAutoFillBackground(True)
p = LAUNCH_FRAME.palette()
p.setColor(LAUNCH_FRAME.backgroundRole(), Qt.black)
LAUNCH_FRAME.setPalette(p)

# Hide mouse pointer
APP.setOverrideCursor(Qt.CursorShape.BlankCursor)

# Setup spinning circle
waiting_circ = QtWaitingSpinner()
waiting_circ.setParent(LAUNCH_FRAME)
waiting_circ.start()

def launch():
    
    import sys
    sys.path.append("/bro/git/py")
    
    print("Launching main program...")
    from main import MAIN_WINDOW, remote
    MAIN_WINDOW.show()
    
    waiting_circ.stop()
    LAUNCH_FRAME.hide()
    
    asyncio.create_task(remote.init())

async def update():
    
    print("Running update script...")
    proc = await asyncio.create_subprocess_exec("update")
    await proc.communicate()
    print("Finished running update script.")
    launch()

def main():
    with qtinter.using_asyncio_from_qt():
        print("Starting launch screen...")
        LAUNCH_FRAME.show()
        asyncio.create_task(update())
        APP.exec_()

main()
print("Exiting launch.py...")