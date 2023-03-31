from calibrate import *


class OriveNEO:

    def __init__(self, odrv):
        self.odrv = odrive.find_any(serial_number=odrv)

    def close_loop_control(self):
        self.odrv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.odrv.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

    def idle_state(self):
        self.odrv.axis0.requested_state = AXIS_STATE_IDLE
        self.odrv.axis1.requested_state = AXIS_STATE_IDLE

    def set_motor_velocity(self, speed):
        self.odrv.axis0.controller.input_vel = speed
        self.odrv.axis1.controller.input_vel = speed


def main():
    odrives = get_all_odrives()
    odrv = odrives[0]
    calibrate_all_motors(odrv)

    neo = OriveNEO(odrv)

    while True:
        print("Spinning")
        neo.close_loop_control()
        neo.set_motor_velocity(5)
        time.sleep(5)
        print("Sleeping")
        neo.set_motor_velocity(0)
        neo.idle_state()
        time.sleep(5)

    

if __name__ == "__main__":
    main()