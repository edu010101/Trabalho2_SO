from typing import List, Dict
import time
from scheduling_simulator.schedulers.processing_info import ProcessingInfo


class BaseProcess:
    def __init__(self, name: str, duration: int, arrival_time: int):
        self.name = name
        self.duration = duration
        self.initial_duration = duration
        self.arrival_time = arrival_time

        self.start_time = 0
        self.end_time = 0

        self.waiting_time = 0
        self.processing_time = 0
        self.turnaround_time = 0
        
        self.is_finished = False
        self.is_started = False

    
    def start(self):
        self.is_started = True

    
    def execute(self, clock_period: float):
        spended_time = min(clock_period, self.duration)
        self.processing_time += spended_time
        self.duration -= clock_period
        
        if self.duration <= 0:
            self.turnaround_time += spended_time
            self.duration = 0
            self.is_finished = True


    def increase_existing_time(self, clock_period: float):
        if not self.is_finished and self.is_started: 
            self.turnaround_time += clock_period


    def get_metrics(self) -> ProcessingInfo:
        self.waiting_time = self.turnaround_time - self.processing_time
        
        return ProcessingInfo(
            name=self.name,
            duration=self.initial_duration,
            arrival_time=self.arrival_time,
            waiting_time=self.waiting_time,
            processing_time=self.processing_time,
            turnaround_time=self.turnaround_time
        ) 

    
    

        


