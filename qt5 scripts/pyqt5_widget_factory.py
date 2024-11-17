from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pyqt5_system_dialogs import *
from PyQt5.QtCore import*


def get_widget(container: QWidget, widget_type: str, geometry: list, label: str,  tag: str=None, **font_info: dict):
    # Create dict whose keys are widget types and whose items are widget constructor functions
    widget_maker = {
        'label': QLabel(),
        'button': QPushButton(),
        'checkbox': QCheckBox(),
        'radiobutton': QRadioButton(),
        'lineedit': QLineEdit(),
        'spinboxint': QSpinBox(),
        'spinboxdbl': QDoubleSpinBox()
    }

    try:
        x_pos, y_pos, width, height = geometry
        if font_info:
            font_family = font_info['family']
            font_size = font_info['size']
            is_bold = font_info['bold']
            is_italic = font_info['italic']
            font = QFont(font_family, font_size)
            if is_bold: font.setBold(True)
            if is_italic: font.setItalic(True)
        else:
            font = None
        
        # Create the widget
        widget = widget_maker[widget_type]
        widget.setParent(container)
        widget.setGeometry(x_pos, y_pos, width, height)
        if label: widget.setText(label)
        if font_info: widget.setFont(font)
        if tag:
            widget.setObjectName(tag)
        
        return widget
    except Exception as e:
        print(f"Error: {e}")
        return None
