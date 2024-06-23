from scheduling_simulator.view.main_menu import MainMenu
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication([])
window = MainMenu()
# for info in infos:
#     window.add_process(info)

window.show()

sys.exit(app.exec())












