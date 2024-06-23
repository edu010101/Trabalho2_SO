from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
from scheduling_simulator.utils import apply_stylesheet
from dataclasses import dataclass
from scheduling_simulator.schedulers.base_process import BaseProcess


class ProcessTable(QListWidget):
    def __init__(self):
        super().__init__()
        self.build()
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QListWidget.SelectionMode.NoSelection)


    def build(self):
        self.setFixedWidth(300)
    
    
    def add_process(self, process: BaseProcess):
        item = ProcessItem(process)
        self.addItem(item)
        widget = ProcessItemWidget(process)
        item.setSizeHint(widget.sizeHint())  # Set the size hint of the item
        self.setItemWidget(item, widget)


    def clear_processes(self):
        self.clear()


class ProcessItem(QListWidgetItem):
    def __init__(self, process: ProcessingInfo):
        super().__init__()
        self.process = process


class ProcessItemWidget(QWidget):
    def __init__(self, process: ProcessingInfo):
        super().__init__()
        self.process = process
        self.build()
        apply_stylesheet(self, "./scheduling_simulator/view/stylesheets/process_result.css")


    def build(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.build_title()
        self.build_labels()
        

    def build_title(self, process_icon_path: str = "./scheduling_simulator/view/icons/cpu_icon.png"):
        #here we gonna have a layout with the icon o left and the text on the right
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        title_icon = QLabel()
        scaled_pixmap = QPixmap(process_icon_path).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Example: scale to 32x32 while keeping aspect ratio
        title_icon.setPixmap(scaled_pixmap)
        title_layout.addWidget(title_icon)

        title_label = QLabel(f"{self.process.name}")
        title_label.setObjectName("title_label")
        title_layout.addWidget(title_label)

        self.layout.addLayout(title_layout)


    def build_labels(self):
        self.arrival_time_label = QLabel(f"Arrival Time: {self.process.arrival_time}")
        self.burst_time_label = QLabel(f"Burst Time: {self.process.duration}")

        self.layout.addWidget(self.arrival_time_label)
        self.layout.addWidget(self.burst_time_label)

        if hasattr(self.process, "priority"):
            self.priority_label = QLabel(f"Priority: {self.process.priority}")
            self.layout.addWidget(self.priority_label)

        self.final_line = QWidget()
        self.final_line.setObjectName("final_line")
        self.layout.addWidget(self.final_line)

