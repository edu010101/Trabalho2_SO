from scheduling_simulator.view.schedulers_menus.base_scheduler_menu import BaseSchedulerMenu
from scheduling_simulator.schedulers.FCFS import FCFSScheduler

CLOCK_TIME = 0.1

class FCFSMenu(BaseSchedulerMenu):
    def __init__(self, process_results_menu):
        super().__init__(process_results_menu)
        self.scheduler = FCFSScheduler(CLOCK_TIME)
        