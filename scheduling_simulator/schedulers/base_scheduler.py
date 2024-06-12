from abc import ABC
from typing import List, Dict
from scheduling_simulator.schedulers.base_process import BaseProcess
import time

class BaseScheduler(ABC):
    def __init__(self):
        self.execution_time = 0

    def run(self, processes: List[BaseProcess]):
        start = time.time()
        for process in processes:
            process.run()
        self.execution_time = time.time() - start

