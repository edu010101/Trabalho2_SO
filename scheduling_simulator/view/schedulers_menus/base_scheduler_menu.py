from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from scheduling_simulator.schedulers.base_scheduler import BaseScheduler
from scheduling_simulator.view.schedulers_menus.process_table import ProcessTable
from scheduling_simulator.utils import read_json_file
from scheduling_simulator.schedulers.base_process import BaseProcess

CLOCK_TIME = 0.1
PROCESS_DEFINITION_PATH = "processes_definition.json"

class BaseSchedulerMenu(QWidget):
    def __init__(self, process_results_menu):
        super().__init__()
        self.scheduler = BaseScheduler(CLOCK_TIME)
        self.process_results_menu = process_results_menu
        self.processes = []
        self.build()

    
    def build(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.build_table()
        self.build_button()
    

    def build_table(self):  
        self.table = ProcessTable()
        self.layout.addWidget(self.table)
        self.build_processes()
        

    def build_processes(self):
        self.processes = []
        self.table.clear_processes()
        process_infos = read_json_file(PROCESS_DEFINITION_PATH)["processes"]
        for process_info in process_infos:
            process = BaseProcess(process_info["name"],  process_info["duration"], process_info["arrival_time"])
            self.processes.append(process)
            self.table.add_process(process)


    def build_button(self):
        self.button = QPushButton("Run")
        self.button.setStyleSheet("""
                                  QPushButton {
                                  background-color: #4CAF50; color: white; border: none; border-radius: 5px; 
                                  padding: 10px 24px; text-align: center; text-decoration: none; display: inline-block; 
                                  font-size: 16px; margin: 4px 2px; cursor: pointer;
                                    }
                                  QPushButton::hover {background-color: #358039;}
                                  """)
        self.button.clicked.connect(self.run)
        
        self.layout.addWidget(self.button)    


    def run(self):
        print("Running" , self.processes)
        self.build_processes()
        self.scheduler.run(self.processes)
        infos = self.scheduler.get_processing_infos()
        self.process_results_menu.clear_processes()
        print(infos)
        for info in infos:
            self.process_results_menu.add_process(info)
        
