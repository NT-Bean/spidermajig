CENTER_OFFSET = 5  # degrees

from adafruit_servokit import ServoKit

import time

kit = ServoKit(channels=16)

servo = kit.servo[0]

# Replace with your discovered values
servo.set_pulse_width_range(500, 2550)
CENTER_OFFSET = -3  # degrees

def corrected_angle(angle):
    if angle <= 120 and angle >= 60:
        return angle * (90 / (90 - CENTER_OFFSET))
    else:
        return angle

for angle in [0, 45, 90, 135, 180, 135, 90, 45, 0]:
    servo.angle = corrected_angle(angle)
    time.sleep(1)
