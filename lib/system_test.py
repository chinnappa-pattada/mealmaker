"""
Notes
Restrict the keywords in each step for simplicity.
if action is "dispense", the supported "wait" keywords is/are "time"
if action is "heat",                   "wait" keywords is/are "temp"

All this will be validated in the recipie before the start
"""

import recipie_reader
import logging
import mealmaker_constants as MMK
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "hw_intf/action_components"))
sys.path.append(os.path.join(os.path.dirname(__file__), "hw_intf/sensor_components"))
import heating_element
import stirrer
import dispenser
import thermal_sensor

RECIPIE = os.path.join(os.path.dirname(__file__), "recipies/salt_water.json")
LOG_FILE = os.path.join(os.path.dirname(__file__), "../log/mm.log")
LOG_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d - %(funcName)20s()] %(levelname)s %(message)s"
logging.basicConfig(filename=LOG_FILE,
                    level=logging.DEBUG, format=LOG_FORMAT)

def get_recipie(recipie=RECIPIE):
    try:
        rec_rdr = recipie_reader.RecipieReader(recipie)
    except IOError as io:
        print 'io: {}'.format(io)
        exit(1)
    except KeyError as ke:
        print 'ke: {}'.format(ke)
        exit(1)

    logging.info('pans: {}'.format(rec_rdr.get_pans()))
    logging.info('ingredient_props: {}'.format(rec_rdr.get_ingredient_props()))
    logging.info('steps: {}'.format(rec_rdr.get_steps()))

    return rec_rdr

def do_steps(steps):
    """
    TODO: Break this out into another module
          return success/failure
    """
    # TODO: use abstraction of the Platform
    # to fetch Platform-specific components
    he_inst = heating_element.HeatingElement()
    stir_inst = stirrer.Stirrer()

    ts_inst = thermal_sensor.ThermalSensor()

    for step in steps:
        step_ing, action, wait_param, wait_val =  step[MMK.KEY_STEP_ING], step[MMK.KEY_ACTION], \
                                                  step[MMK.KEY_WAIT_PARAM], step[MMK.KEY_WAIT_VALUE]

        logging.info("Step Action: {}".format(action))
        if action == "dispense":
            for ing in step_ing:
                disp_id = ing_prop[ing][MMK.KEY_DISPENSER]
                disp = dispenser.Dispenser(disp_id)
                disp.dispense()
                logging.info('Dispensed {} from Dispenser {}'.format(ing, disp_id))

            logging.info('Wait {} for {}: start'.format(wait_val, wait_param))
            time.sleep(wait_val)
            logging.info('Wait {} for {}: stop'.format(wait_val, wait_param))

        elif action == "heat":
            curr_temp = ts_inst.get_temp()
            logging.info("Current Temperature: {}".format(curr_temp))
            logging.info('Wait {} for {}: start'.format(wait_val, wait_param))
            if curr_temp < wait_val:
                he_inst.heat_on()
                while curr_temp < wait_val:
                    # TODO exit strategy
                    time.sleep(3)
                    # curr_temp = ts_inst.get_temp()
                    curr_temp = ts_inst.get_test_temp_high()
            else:
                he_inst.heat_off()
                while curr_temp > wait_val:
                    # TODO exit strategy
                    time.sleep(3)
                    # curr_temp = ts_inst.get_temp()
                    curr_temp = ts_inst.get_test_temp_low()
            logging.info("Current Temperature: {}".format(curr_temp))

    return None

if __name__ == "__main__":
    rec_rdr = get_recipie(RECIPIE)
    pans = rec_rdr.get_pans()
    ing_prop = rec_rdr.get_ingredient_props()
    steps = rec_rdr.get_steps()

    do_steps(steps)
