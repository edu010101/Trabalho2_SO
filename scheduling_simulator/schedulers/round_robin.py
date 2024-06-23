from abc import ABC
from typing import List, Dict
from scheduling_simulator.schedulers.base_process import BaseProcess
from scheduling_simulator.schedulers.base_scheduler import BaseScheduler
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
from queue import Queue

class RoundRobinScheduler(BaseScheduler):
    def __init__(self, quantum: float):
        super().__init__(quantum)

    def run(self, processes: List[BaseProcess]):
        current_time = 0
        self.processing_infos = []
        process_queue = Queue()

        for process in processes:
            process_queue.put(process)
        
        for process in processes:
            if (current_time >= process.arrival_time):
                process.start()
        
        while not process_queue.empty():
            process = process_queue.get()
            if process.is_finished:
                continue
            
            if (current_time >= process.arrival_time) and (not process.is_started):
                process.start()
            
            if (process.is_started) and (not process.is_finished):
                execution_time = min(self.clock_period, process.duration)
                process.execute(execution_time)            
            
                for subprocess in processes:
                    if subprocess.is_finished or not subprocess.is_started:
                        continue
                    subprocess.increase_existing_time(execution_time)
            
            if process.duration > 0:
                process_queue.put(process)
            else:
                self.processing_infos.append(process.get_metrics())

            current_time += self.clock_period
        
    def get_processing_infos(self) -> List[ProcessingInfo]:
        return self.processing_infos

    def set_clock_period(self, clock_period: float):
        self.clock_period = clock_period
        