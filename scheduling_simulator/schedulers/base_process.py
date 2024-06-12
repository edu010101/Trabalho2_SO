from typing import List, Dict
import time

class BaseProcess:
    def __init__(self, name: str, duration: int, arrival_time: int):
        self.name = name
        self.duration = duration
        self.arrival_time = arrival_time
        self.start_time = 0
        self.end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    def start(self):
        self.start_time = time.time()

    def execute(self, clock_period: float):
        self.duration -= clock_period
        if self.duration <= 0:
            self.duration = 0
            self.end_time = time.time()
            self.turnaround_time = self.end_time - self.arrival_time
        else:
            self.waiting_time += clock_period

    def get_metrics(self) -> Dict[str, float]:
        
        
        
        
        return {
            "waiting_time": self.waiting_time,
            "turnaround_time": self.turnaround_time
        }
    

        


