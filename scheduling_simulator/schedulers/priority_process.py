from typing import List, Dict
import time
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
from scheduling_simulator.schedulers.base_process import BaseProcess

class PriorityProcess(BaseProcess):
    def __init__(self, name: str, duration: int, arrival_time: int, priority: int):
        super().__init__(name, duration, arrival_time)
        self.priority = priority
        