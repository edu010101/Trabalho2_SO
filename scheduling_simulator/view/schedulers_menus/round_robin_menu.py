from scheduling_simulator.view.schedulers_menus.base_scheduler_menu import BaseSchedulerMenu
from scheduling_simulator.schedulers.round_robin import RoundRobinScheduler
from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QLabel

QUANTUM = 20

class RoundRobinMenu(BaseSchedulerMenu):
    def __init__(self, process_results_menu):
        super().__init__(process_results_menu)
        self.scheduler = RoundRobinScheduler(QUANTUM)


    def build(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.build_quantum_selector()
        self.build_table()
        self.build_button()

    def build_quantum_selector(self):
        quantum_title = QLabel("Defina o valor do quantum")
        self.quantum_selector = QLineEdit()
        self.quantum_selector.setText(str(QUANTUM))
        self.layout.addWidget(quantum_title)
        self.layout.addWidget(self.quantum_selector)

    def run(self):
        self.build_processes()
        self.process_results_menu.clear_processes()

        print("Running" , self.processes)
        if not(self.quantum_selector.text() != "" and self.quantum_selector.text().isdigit()):
            return
        
        quantum_value = max(int(self.quantum_selector.text()), 0.001)
        
        self.scheduler.set_clock_period(quantum_value)
        self.scheduler.run(self.processes)
        infos = self.scheduler.get_processing_infos()
        
        print(infos)
        for info in infos:
            self.process_results_menu.add_process(info)