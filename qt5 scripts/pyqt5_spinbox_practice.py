import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pyqt5_system_dialogs import *
from PyQt5.QtCore import*
from pyqt5_widget_factory import *
import re

# Mass:
# 1 lb= 0.4535923kg
# 1 kg= 2.2lb

# Temp: 
# F->C (F-32)/1.8
# C->F C * 1.8 + 32

# Length:
# Feet = Meters * 3.28
# Meters = Feet/3.28


LBS_TO_KGS = 0.45
KGS_TO_LBS = 2.21
FEET_TO_METERS = 0.3
METERS_TO_FEET = 3.28
MAX_UNIT_VAL = 100_001.00



MSG_BOX_TITLE = "PyQt5 Practice"

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        self.configure_environment()
        self.create_spinboxes()
        self.create_radiobuttons()
        self.create_buttons()
        self.config_spinboxes()


    def configure_environment(self):
        self.resize(500, 500)
        self.setWindowTitle("Spinbox Practice")
    

    def create_spinboxes(self):
        # Create two double spinbox controls: each of which can be
        # used for Imperial or Metric units

        self.sbxFromUnit = get_widget(
            self,
            'spinboxdbl',
            [20, 100, 220, 20],
            '',
            'from_unit',
            family='Times',
            size=14,
            bold=False,
            italic=False
        )

        # Form is initialized to convert weights Imperial to Metric
        self.sbxFromUnit.setMinimum(0.0)
        self.sbxFromUnit.setMaximum(MAX_UNIT_VAL)
        self.sbxFromUnit.valueChanged.connect(self.sbx_ValueChanged)

        self.sbxToUnit = get_widget(
            self,
            'spinboxdbl',
            [260, 100, 220, 20],
            '',
            'to_unit',
            family='Times',
            size=14,
            bold=False,
            italic=False
        )
        self.sbxToUnit.setMinimum(0.0)
        self.sbxToUnit.setMaximum(MAX_UNIT_VAL)
        self.sbxToUnit.valueChanged.connect(self.sbx_ValueChanged)
    

    def create_radiobuttons(self):
        # Create a group of buttons for the various 
        # types of conversion
        self.btn_group_units = QButtonGroup()

        self.optWeight = get_widget(self,
                                'radiobutton',
                                [20, 150, 200, 20],
                                'Weight',
                                'weight',
                                family='Consolas',
                                size=14,
                                bold=False,
                                italic=True)
        self.optWeight.setChecked(True)
        self.optWeight.clicked.connect(self.opt_btn_onClick)
        self.btn_group_units.addButton(self.optWeight)

        self.optTemp = get_widget(self,
                                'radiobutton',
                                [20, 180, 200, 20],
                                'Temperature',
                                'temperature',
                                family='Consolas',
                                size=14,
                                bold=False,
                                italic=True)
        self.optTemp.clicked.connect(self.opt_btn_onClick)
        self.btn_group_units.addButton(self.optTemp)

        self.optLength = get_widget(self,
                                'radiobutton',
                                [20, 210, 200, 20],
                                'Length',
                                'length',
                                family='Consolas',
                                size=14,
                                bold=False,
                                italic=True)
        self.optLength.clicked.connect(self.opt_btn_onClick)
        self.btn_group_units.addButton(self.optLength)

        # Create a group of buttons for the conversion direction
        self.btn_group_conversion = QButtonGroup()

        self.optImperial_Metric = get_widget(self,
                                'radiobutton',
                                [240, 150, 200, 20],
                                'Imperial->Metric',
                                'to_metric',
                                family='Consolas',
                                size=14,
                                bold=False,
                                italic=True)
        self.optImperial_Metric.setChecked(True)
        self.optImperial_Metric.clicked.connect(self.opt_btn_onClick)
        self.btn_group_conversion.addButton(self.optImperial_Metric)

        self.optMetric_Imperial = get_widget(self,
                                'radiobutton',
                                [240, 180, 200, 20],
                                'Metric->Imperial',
                                'to_imperial',
                                family='Consolas',
                                size=14,
                                bold=False,
                                italic=True)
        self.optMetric_Imperial.clicked.connect(self.opt_btn_onClick)
        self.btn_group_conversion.addButton(self.optMetric_Imperial)


    def create_buttons(self):
        self.btnReset = get_widget(
            self,
            'button',
            [300, 20, 150, 40],
            'Reset',
            'reset',
            family='Arial',
            size=14,
            bold=False,
            italic=False
        )
        self.btnReset.setToolTip('Set spinboxes to 0 and select Imperial to Metric Weight conversion')
        self.btnReset.clicked.connect(self.btnReset_onClick)



    def config_spinboxes(self, conversion_type="Weight", conversion_direction="imperial to metric"):
        labels_dict = {
            'imperial to metric': 
                {'Weight': [' lbs', ' kgs'], 
                'Temperature': [f" {chr(0x00B0)}F", f" {chr(0x00B0)}C"], 
                'Length': [' ft', ' m']},

            'metric to imperial': 
                {'Weight': [' kgs', ' lbs'], 
                'Temperature': [f" {chr(0x00B0)}C", f" {chr(0x00B0)}F"], 
                'Length': [' m', ' ft']}
        }
        
        # Set the labels for the spinboxes and also the minimum values
        # Only temperature can be negative
        spin_button_labels = labels_dict[conversion_direction][conversion_type]
        min_val = -100.0 if conversion_type == "Temperature" else 0.0
        prefix = conversion_type + ": "
        self.sbxFromUnit.setPrefix(prefix)
        self.sbxFromUnit.setSuffix(spin_button_labels[0])
        self.sbxFromUnit.setMinimum(min_val)
        self.sbxToUnit.setPrefix(prefix)
        self.sbxToUnit.setSuffix(spin_button_labels[1])
        self.sbxToUnit.setMinimum(min_val)



    def get_conversion_settings(self):
        conversion_direction = "imperial to metric" if self.optImperial_Metric.isChecked() else "metric to imperial"
        for button in [self.optWeight, self.optTemp, self.optLength]:
            if button.isChecked():
                conversion_type = button.objectName().capitalize()
                break
        return (conversion_type, conversion_direction)

    
    def convert_units(self, conversion_type, conversion_direction):
        conversion_dict = {
            'imperial to metric': 
                {'Weight': lambda from_weight: from_weight * LBS_TO_KGS, 
                'Temperature': lambda from_temp: (from_temp-32)/1.8, 
                'Length': lambda from_length: from_length * FEET_TO_METERS},

            'metric to imperial': 
                {'Weight': lambda from_weight: from_weight * KGS_TO_LBS, 
                'Temperature': lambda from_temp: (from_temp * 1.8) + 32, 
                'Length': lambda from_length: from_length * METERS_TO_FEET}
        }

        converted_value = conversion_dict[conversion_direction][conversion_type](self.sbxFromUnit.value())
        self.sbxToUnit.setValue(converted_value)

    
    
    def opt_btn_onClick(self):
        conversion_type, conversion_direction = self.get_conversion_settings()
        self.config_spinboxes(conversion_type, conversion_direction)
        # Perform the conversion and update the spinboxes accordingly
        self.convert_units(conversion_type, conversion_direction)
    


    def sbx_ValueChanged(self):
        if self.sender().objectName() == "from_unit":
            if self.sbxFromUnit.value() > MAX_UNIT_VAL - 1:
                msgAttention(self, "Unit Convertor", f"Input cannot exceed {MAX_UNIT_VAL - 1}.")
                return
        conversion_type, conversion_direction = self.get_conversion_settings()
        self.convert_units(conversion_type, conversion_direction)

        # print(f"{self.sender().objectName()} spinbox changed value")

    
    def btnReset_onClick(self):
        # Set spinboxes to 0
        # Set conversion type to Weight
        # Set conversion direction to Imperial->Metric
        self.sbxFromUnit.setValue(0.0)
        self.sbxToUnit.setValue(0.0)
        self.optWeight.setChecked(True)
        self.optImperial_Metric.setChecked(True)
        self.config_spinboxes()


       


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
