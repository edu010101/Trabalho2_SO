from scheduling_simulator.view.schedulers_menus.base_scheduler_menu import BaseSchedulerMenu
from scheduling_simulator.schedulers.SJF_preemp import SJFPreempScheduler

CLOCK_TIME = 0.1

class SJFPreempMenu(BaseSchedulerMenu):
    def __init__(self, process_results_menu):
        super().__init__(process_results_menu)
        self.scheduler = SJFPreempScheduler(CLOCK_TIME)
