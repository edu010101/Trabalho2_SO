from PyQt6.QtWidgets import QWidget

def apply_stylesheet(widget: QWidget, stylesheet_path: str):
    with open(stylesheet_path, "r") as file:
        stylesheet = file.read()
        widget.setStyleSheet(stylesheet)

