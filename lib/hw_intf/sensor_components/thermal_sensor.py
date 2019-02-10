"""
Thermal Sensor
"""
import os
import sys
# import thermal sensor from hardware/sensors/mlx90614
sys.path.append(os.path.join(os.path.dirname(__file__), "../abcs"))

# ABC for thermal sensors
from ts_abc import TS_ABC

class ThermalSensor(TS_ABC):
    """
    Thermal Sensor Class
    """

    def get_temp(self):
        """
        Implementing abstract method
        """
        print "Temperature is tbd"

    def get_test_temp_high(self):
        """
        TODO: Delete Test Function
        """
        return 101

    def get_test_temp_low(self):
        """
        TODO: Delete Test Function
        """
        return 78
