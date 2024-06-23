from abc import ABC
from typing import List, Dict
from scheduling_simulator.schedulers.base_process import BaseProcess
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
from queue import Queue

class SJFPreempScheduler(ABC):
    def __init__(self, clock_period: float):
        self.execution_time = 0
        self.clock_period = clock_period
        self.processing_infos = []

    def run(self, processes: List[BaseProcess]):
        processes_queue = []
        current_time = 0
        self.processing_infos = []

        for process in processes:
            if process.is_finished:
                continue
            
            if (current_time >= process.arrival_time) and (not process.is_started):
                process.start()
                processes_queue.append(process)
        
        processes.sort(key=lambda x: x.duration) # Ordena os processos por duração

        while len(processes_queue) > 0:
            current_time += self.clock_period
            
            # Loop para adicionar os processos conforme a chegada
            for process in processes:
                if process.is_finished:
                    continue
                
                if (current_time >= process.arrival_time) and (not process.is_started):
                    process.start()
                    processes_queue.append(process)

                process.increase_existing_time(self.clock_period)

            # Loop para executar os processos
            if len(processes_queue) > 0:
                processes_queue[0].execute(self.clock_period)

                if processes_queue[0].is_finished:
                    processed = processes_queue.pop(0)
                    processes.remove(processed)
                    self.processing_infos.append(processed.get_metrics())

            processes_queue.sort(key=lambda x: x.duration) # Ordena os processos por duração
                    

    def get_processing_infos(self) -> List[ProcessingInfo]:
        return self.processing_infos