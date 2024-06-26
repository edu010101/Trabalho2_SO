from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from scheduling_simulator.schedulers.processing_info import ProcessingInfo
from scheduling_simulator.utils import apply_stylesheet

class ProcessResultsMenu(QListWidget):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.processes = []
        self.setFixedWidth(300)
    
    
    def add_process(self, process: ProcessingInfo):
        self.processes.append(process)
        item = ProcessResultItem(process)
        self.addItem(item)
        widget = ProcessResultItemWidget(process)
        item.setSizeHint(widget.sizeHint())  # Set the size hint of the item
        self.setItemWidget(item, widget)
    

    def clear_processes(self):
        self.processes = []
        self.clear()


class ProcessResultItem(QListWidgetItem):
    def __init__(self, process: ProcessingInfo):
        super().__init__()
        self.process = process


class ProcessResultItemWidget(QWidget):
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
        

    def build_title(self, process_icon_path: str = "./scheduling_simulator/view/icons/process_icon.png"):
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
        self.turnaround_time_label = QLabel(f"Turnaround Time: {round(self.process.turnaround_time, 2)}")
        self.waiting_time_label = QLabel(f"Waiting Time: {round(self.process.waiting_time, 2)}")
        self.processing_time_label = QLabel(f"Processing Time: {round(self.process.processing_time, 2)}")

        self.layout.addWidget(self.turnaround_time_label)
        self.layout.addWidget(self.waiting_time_label)
        self.layout.addWidget(self.processing_time_label)

        self.final_line = QWidget()
        self.final_line.setObjectName("final_line")
        self.layout.addWidget(self.final_line)
        

