"Development test module for SSR control"
import os
import sys
from time import sleep
sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
import pi_ssr as SSR
sys.path.append(os.path.join(os.path.dirname(__file__), "../sensors/temperature"))
import mlx90614 as MLX

# Max and Min temperatures in degrees C
TEMP_MIN = 32
TEMP_MAX = 36

def main():
    "Keep temperature of stove in between TEMP_MIN and TEMP_MAX degrees C"
    print 'TEMP_MIN: {}; TEMP_MAX: {}'.format(TEMP_MIN, TEMP_MAX)
    temp_sensor = MLX.MLX90614()
    try:
        while 1:
            stove_temp = temp_sensor.get_obj_temp()
            if stove_temp < TEMP_MIN:
                print 'Temp. is {}; Raising it.'.format(stove_temp)
                SSR.ssr_on()
            elif stove_temp > TEMP_MAX:
                print 'Temp. is {}; Lowering it.'.format(stove_temp)
                SSR.ssr_off()
            else:
                print 'Temp. is {}'.format(stove_temp)

            sleep(3)
        
    except KeyboardInterrupt:
        SSR.ssr_off()

if __name__ == "__main__":
    main()
