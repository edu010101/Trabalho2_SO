from scheduling_simulator.view.schedulers_menus.base_scheduler_menu import BaseSchedulerMenu
from scheduling_simulator.schedulers.priority import PriorityScheduler
from scheduling_simulator.view.schedulers_menus.process_table import ProcessTable
from scheduling_simulator.utils import read_json_file
from scheduling_simulator.schedulers.priority_process import PriorityProcess

PROCESS_DEFINITION_PATH = "processes_definition.json"
CLOCK_TIME = 0.1

class PriorityMenu(BaseSchedulerMenu):
    def __init__(self, process_results_menu):
        super().__init__(process_results_menu)
        self.scheduler = PriorityScheduler(CLOCK_TIME)

    
    def build_processes(self):
        self.processes = []
        self.table.clear_processes()
        process_infos = read_json_file(PROCESS_DEFINITION_PATH)["processes"]
        for process_info in process_infos:
            process = PriorityProcess(process_info["name"], 
                                    process_info["duration"],
                                    process_info["arrival_time"],
                                    process_info["priority"])
            self.processes.append(process)
            self.table.add_process(process)