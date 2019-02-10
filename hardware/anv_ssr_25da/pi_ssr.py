"Pi Module to control the SSR"
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../pi"))
import pi_gpio_apis as API
import json

# TODO
# Read designated GPIO pin from config file
SSR_GPIO = 11

def turn_on():
    """
    Turn on the SSR
    :return int ret_code: 0 if successfully turned on
                          1 for failure
    """
    ret_code = 1
    API.gpio_setup()
    ret_code = API.gpio_on(SSR_GPIO)
    return ret_code

def turn_off():
    """
    Turn off the SSR
    :return int ret_code: 0 if successfully turned on
                          1 for failure    API.gpio_setup()
    """
    ret_code = 1
    ret_code = API.gpio_off(SSR_GPIO)
    API.gpio_cleanup()
    return ret_code
