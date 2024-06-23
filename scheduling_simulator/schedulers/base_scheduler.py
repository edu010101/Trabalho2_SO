from abc import ABC
from typing import List, Dict
from scheduling_simulator.schedulers.base_process import BaseProcess
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
import time

class BaseScheduler(ABC):
    def __init__(self, clock_period: float):
        self.execution_time = 0
        self.clock_period = clock_period
        self.processing_infos = []

    def run(self, processes: List[BaseProcess]):
        current_time = 0
        self.processing_infos = []

        for process in processes:
            if (current_time >= process.arrival_time):
                process.start()

        while any([not process.is_finished for process in processes]):
            current_time += self.clock_period
            
            for process in processes:
                if process.is_finished:
                    continue
                
                if (current_time >= process.arrival_time) and (not process.is_started):
                    process.start()

                for subprocess in processes:
                    if subprocess.is_finished or not subprocess.is_started:
                        continue
                    
                    subprocess.increase_existing_time(self.clock_period)

                if (process.is_started) and (not process.is_finished):
                    process.execute(self.clock_period)

        for process in processes:
            self.processing_infos.append(process.get_metrics())

    def get_processing_infos(self) -> List[ProcessingInfo]:
        return self.processing_infos
