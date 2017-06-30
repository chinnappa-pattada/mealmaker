"SSR Functional Test Module" 
import os
import sys
import pi_ssr as SSR

def main():
	"Turn SSR on until ^C pressed"
	print 'starting test'
	try:
		while(1):
			SSR.ssr_on()
	except KeyboardInterrupt():
		SSR.ssr_off()

if __name__ == "__main__":
	main()
