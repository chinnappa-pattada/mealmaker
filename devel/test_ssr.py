"Development test module for SSR control"
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
import pi_ssr as SSR

def main():
    "Keep SSR on until keyboard exit"
    print 'starting test'
    try:
        while 1:
            SSR.ssr_on()
    except KeyboardInterrupt:
        SSR.ssr_off()

if __name__ == "__main__":
    main()
