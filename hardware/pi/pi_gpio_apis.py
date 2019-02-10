"""
R PI GPIO functions
"""
import RPi.GPIO as GPIO

def gpio_on(gpio_pin):
    """
    Turn on specified GPIO pin

    :param int gpio_pin: GPIO pin to turn on
    :return int ret_code: 0 if successfully turned on
                          1 for failure
    """
    # TODO
    # check for PI version
    # check for range of gpio pins
    ret_code = 1
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, True)
    # input should be high for 'True' output pin
    pin_val = GPIO.input(gpio_pin)
    if pin_val == 1:
        ret_code = 0

    return ret_code

def gpio_off(gpio_pin):
    """
    Turn off specified GPIO pin
    :param int gpio_pin: GPIO pin to turn off
    :return int ret_code: 0 if successfully turned off
                          1 for failure
    """
    ret_code = 1
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, False)
    # input should be low for 'False' output pin
    pin_val = GPIO.input(gpio_pin)
    if pin_val == 0:
        ret_code = 0

    return ret_code

def gpio_setup():
    "Initial GPIO setup"
    GPIO.setmode(GPIO.BOARD)

def gpio_cleanup():
    "Cleanup GPIO"
    GPIO.cleanup()
