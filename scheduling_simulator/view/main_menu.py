from PyQt6.QtWidgets import QMainWindow
from scheduling_simulator.view.schedulers_types import SchedulersTypesMenu
from scheduling_simulator.view.process_results import ProcessResultsMenu


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scheduling Simulator")
    
