"R PI GPIO functions"
import RPi.GPIO as GPIO

def gpio_on(gpio_pin):
    "Turn on specified GPIO pin"
    # TODO
    # check for PI version
    # check for range of gpio pins
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, True)

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
