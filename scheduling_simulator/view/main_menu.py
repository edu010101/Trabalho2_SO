from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from scheduling_simulator.view.schedulers_types import SchedulerTypesMenu
from scheduling_simulator.view.process_results import ProcessResultsMenu


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scheduling Simulator")
        self.setFixedSize(869, 600)
        self.build()


    def build(self):
        self.main_layout = QHBoxLayout()
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.main_layout)


        self.process_results_menu = ProcessResultsMenu()
        self.schedulers_types_menu = SchedulerTypesMenu(self.process_results_menu)
        
        self.main_layout.addWidget(self.schedulers_types_menu)
        self.main_layout.addWidget(self.process_results_menu)

        
