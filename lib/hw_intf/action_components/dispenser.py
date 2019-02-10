"""
Dispenser
"""
# import Dispenser-Motor class
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../abcs"))
from disp_abc import DISP_ABC

class Dispenser(DISP_ABC):
    """
    Dispenser Class
    """

    def __init__(self, disp_id):
        """
        init function for Dispenser Class

        Calibrate by moving all(?) Dispensers to resting location
        """
        # for dispenser(s?)
        self.calibrate()
        self.disp_id = disp_id
        # TODO:
        # self.motor = motor(<calculate addr from disp_id>)

    def calibrate(selfs):
        """
        Calibrate Dispenser to default location
        """

    def dispense(self):
        """
        Basic dispensing algorithm
        """
        print 'DISPENSER: {} dispensed'.format(self.disp_id)
