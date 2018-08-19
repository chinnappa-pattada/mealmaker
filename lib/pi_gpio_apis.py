"""
R PI GPIO functions
"""
import RPi.GPIO as GPIO

def gpio_on(gpio_pin):
    """
    Turn on specified GPIO pin

    :input int gpio_pin: pin to turn on
    :return: 0 if successfully turned on
             1 for failure
    """
    # TODO
    # check for PI version
    # check for range of gpio pins
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, True)
    return GPIO.input(gpio_pin)


def gpio_off(gpio_pin):
    "Turn off specified GPIO pin"
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, False)

def gpio_setup():
    "Initial GPIO setup"
    GPIO.setmode(GPIO.BOARD)

def gpio_cleanup():
    "Cleanup GPIO"
    GPIO.cleanup()
