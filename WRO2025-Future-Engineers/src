from robot_hat import Pin, ADC, PWM, Servo, fileDB
from robot_hat import utils
import time
import os

# To constrain a value between a minimun and a maximun
def constrain(x, mn, mx):
    return max(mn, min(mx, x))

class Astro(object):

    DIR_MIN = -30
    DIR_MAX = 30

    PERIOD = 4095
    PRESCALER = 10

    def __init__(self, 
                servo_pin:list=['P0'],
                motor_pins:list=['D5', 'P12'],
                ):

        # reset robot_hat
        utils.reset_mcu()
        time.sleep(0.2)

        # DIRECTION SERVO INIT
        self.dir_servo_pin = Servo(servo_pin[0])
        # get calibration values
        self.dir_cali_val = 0
        # set servos to init angle
        self.dir_servo_pin.angle(self.dir_cali_val)

        # MOTOR INIT
        self.rear_dir_pin = Pin(motor_pins[0])
        self.rear_pwm_pin = PWM(motor_pins[1])
        self.motor_direction_pins = [self.rear_dir_pin]
        self.motor_speed_pins = [self.rear_pwm_pin]
        
        # GET CALIBRATION VALUES
        self.cali_dir_value = "[1, 1]"
        self.cali_dir_value = [int(i.strip()) for i in self.cali_dir_value.strip().strip("[]").split(",")]
        self.cali_speed_value = [0, 0]
        self.dir_current_angle = 0
        
        # INIT PWM
        for pin in self.motor_speed_pins:
            pin.period(self.PERIOD)
            pin.prescaler(self.PRESCALER)
        
        
    def set_motor_speed(self, speed):
        speed = constrain(speed, -100, 100)
        
        if speed >= 0:
            direction = 1 * self.cali_dir_value[0]
        elif speed < 0:
            direction = -1 * self.cali_dir_value[0]
        speed = abs(speed)
        
        if speed != 0:
            speed = int(speed /2 ) + 50
        speed = speed - self.cali_speed_value[0]
        if direction < 0:
            self.motor_direction_pins[0].high()
            self.motor_speed_pins[0].pulse_width_percent(speed)
        else:
            self.motor_direction_pins[0].low()
            self.motor_speed_pins[0].pulse_width_percent(speed)

    def motor_speed_calibration(self, value):
        self.cali_speed_value = value
        if value < 0:
            self.cali_speed_value[0] = 0
            self.cali_speed_value[1] = abs(self.cali_speed_value)
        else:
            self.cali_speed_value[0] = abs(self.cali_speed_value)
            self.cali_speed_value[1] = 0

    def motor_direction_calibrate(self, value):
        # set motor direction calibration value
        if value == 1:
            self.cali_dir_value[0] = 1
        elif value == -1:
            self.cali_dir_value[0] = -1

    def dir_servo_calibrate(self, value):
        self.dir_cali_val = value
        self.dir_servo_pin.angle(value)

    def set_dir_servo_angle(self, value):
        self.dir_current_angle = constrain(value, self.DIR_MIN, self.DIR_MAX)
        angle_value  = self.dir_current_angle + self.dir_cali_val
        self.dir_servo_pin.angle(angle_value)

    def set_power(self, speed):
        self.set_motor_speed(1, speed)
        self.set_motor_speed(2, speed)

    def backward(self, speed):
        self.set_motor_speed(-1*speed)

    def forward(self, speed):
        self.set_motor_speed(speed)                 

    def stop(self):
        # Execute twice to make sure it stops
        for _ in range(2):
            self.motor_speed_pins[0].pulse_width_percent(0)
            time.sleep(0.002)


    def reset(self):
        self.stop()
        self.set_dir_servo_angle(0)

if __name__ == "__main__":
	bot = Astro()
	bot.forward(50)
	time.sleep(1)
	bot.stop()
