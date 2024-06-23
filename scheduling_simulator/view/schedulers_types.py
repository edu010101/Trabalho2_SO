from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QTabWidget
from scheduling_simulator.view.schedulers_menus import FCFSMenu, PriorityMenu, RoundRobinMenu, SJFMenu, SJFPreempMenu


class SchedulerTypesMenu(QTabWidget):
    def __init__(self, process_results_menu: QWidget):
        super().__init__()
        self.process_results_menu = process_results_menu
        self.build()
        self.setStyleSheet("font-size: 20px; font-weight: bold;")

    def build(self):
        self.build_fcfs()
        self.build_sjf()
        self.build_sjf_preemp()
        self.build_priority()
        self.build_round_robin()

    def build_fcfs(self):
        self.fcfs_menu = FCFSMenu(self.process_results_menu)
        self.addTab(self.fcfs_menu, "FCFS")

    def build_sjf(self):
        self.sjf_menu = SJFMenu(self.process_results_menu)
        self.addTab(self.sjf_menu, "SJF")

    def build_sjf_preemp(self):
        self.sjf_preemp_menu = SJFPreempMenu(self.process_results_menu)
        self.addTab(self.sjf_preemp_menu, "SJF Preemptive")

    def build_priority(self):
        self.priority_menu = PriorityMenu(self.process_results_menu)
        self.addTab(self.priority_menu, "Priority")

    def build_round_robin(self):
        self.round_robin_menu = RoundRobinMenu(self.process_results_menu)
        self.addTab(self.round_robin_menu, "Round Robin")

    

    

    