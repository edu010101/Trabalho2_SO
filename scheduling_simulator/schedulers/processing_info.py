from dataclasses import dataclass

@dataclass
class ProcessingInfo:
    name: str
    duration: int
    arrival_time: int
    waiting_time: int = 0
    processing_time: int = 0
    turnaround_time: int = 0

    def __str__(self):
        return f"Process {self.name}, Arrival Time: {self.arrival_time}, Duration: {self.duration}, Waiting Time: {self.waiting_time}, Processing Time: {self.processing_time}, Turnaround Time: {self.turnaround_time}"