"Pi Module to control the SSR"
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))
import pi_apis
import json

# TODO
# Read designated GPIO pin from config file
SSR_GPIO = 11

def ssr_on():
	"Turn on the SSR"
	gpio_on(SSR_GPIO)

def ssr_off():
	"Turn off the SSR"
	gpio_off(SSR_GPIO)
	
