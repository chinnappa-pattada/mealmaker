"""
Heating Element

"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../hardware/anv_ssr_25da"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../abcs"))
# Solid State Relay
# import pi_ssr as SSR
# ABC for heating elements
from he_abc import HE_ABC

# TODO: Handle multiple HEs

class HeatingElement(HE_ABC):
    """
    Heating Element Class
    """

    def __init__(self):
        """
        init function for Heating Element Class
        initialize state to 0 (off)
        """
        self.state = 0

    def get_state():
        """
        Fetch state of Heating Element
        :return int state: 0 if HE is off
                           1 if HE is on
        """
        return self.state

    def turn_on():
        """
        Turn on the Heating Element
        """
        # SSR.turn_on()

    def turn_off():
        """
        Turn off the Heating Element
        """
        # SSR.turn_off()

    def heat_on(self):
        """
        Implementing abstract method
        """
        print "Heating Element is On"

    def heat_off(self):
        """
        Implementing abstract method
        """
        print "Heating Element is Off"
