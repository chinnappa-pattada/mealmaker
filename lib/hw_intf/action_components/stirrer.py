"""
Stirrer with location in 3D cartesian space
"""
# import Stirrer-Motor class
# define limits of cartesian space for the stirrer
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../abcs"))
from stir_abc import STIR_ABC

class Stirrer(STIR_ABC):
    """
    Stirrer Class
    """

    def __init__(self, location="default"):
        """
        init function for Stirrer Class

        Calibrate by moving to resting location
        """
        self.calibrate()

    def calibrate(self):
        """
        Calibrate Stirrer to default location
        """

    def stir(self):
        """
        Basic stirring algorithm
        """
