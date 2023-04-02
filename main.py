from calibrate import *

def main():
    odrives = get_all_odrives()
    odrv = odrives[0]
    calibrate_all_motors(odrv)

    odrvControl = odrive.find_any(serial_number=odrv)


    while True:
        print("Boom")
        odrvControl.axis0.controller.input_vel = 5
        odrvControl.axis1.controller.input_vel = 5
        odrvControl.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        odrvControl.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        time.sleep(3)
        odrvControl.axis0.requested_state = AXIS_STATE_IDLE
        odrvControl.axis1.requested_state = AXIS_STATE_IDLE

    

if __name__ == "__main__":
    main()