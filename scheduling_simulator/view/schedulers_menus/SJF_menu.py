from scheduling_simulator.view.schedulers_menus.base_scheduler_menu import BaseSchedulerMenu
from scheduling_simulator.schedulers.SJF import SJFScheduler

CLOCK_TIME = 0.1

class SJFMenu(BaseSchedulerMenu):
    def __init__(self, process_results_menu):
        super().__init__(process_results_menu)
        self.scheduler = SJFScheduler(CLOCK_TIME)