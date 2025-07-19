# SPDX-FileCopyrightText: 2025 John Gale
#
# SPDX-License-Identifier: MIT

"""Brass Instrument Valve Servo Control"""

import time
import board
import digitalio

from adafruit_servokit import ServoKit

# 2D matrix for servo positions[servo#][up, down, or clear]
positions = [[55, 78, 0], [45, 22, 100], [45, 25, 100]]

up_valve = 0
down_valve = 1
clear_valve = 2

# Initialize PCA9685 8-channel Servo FeatherWing
kit = ServoKit(channels=8)
kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].actuation_range = 100
kit.servo[0].angle = positions[0][clear_valve]
kit.servo[1].set_pulse_width_range(1000, 2000)
kit.servo[1].actuation_range = 100
kit.servo[1].angle = positions[1][clear_valve]
kit.servo[2].set_pulse_width_range(1000, 2000)
kit.servo[2].actuation_range = 100
kit.servo[2].angle = positions[2][clear_valve]

# Initialize inputs for 4 switch inputs for valve servo control
n_switch = digitalio.DigitalInOut(board.A0)
n_switch.direction = digitalio.Direction.INPUT
n_switch.pull = digitalio.Pull.UP

s_switch = digitalio.DigitalInOut(board.A1)
s_switch.direction = digitalio.Direction.INPUT
s_switch.pull = digitalio.Pull.UP

w_switch = digitalio.DigitalInOut(board.A2)
w_switch.direction = digitalio.Direction.INPUT
w_switch.pull = digitalio.Pull.UP

e_switch = digitalio.DigitalInOut(board.A3)
e_switch.direction = digitalio.Direction.INPUT
e_switch.pull = digitalio.Pull.UP

# Lookup table for converting the 16 switch states to valve states
# valve_lut = [0, 1, 0, 0, 5, 3, 7, 0, 4, 2, 6, 0, 0, 0, 0, 0]
valve_lut = [
    0b000,
    0b001,
    0b000,
    0b000,
    0b101,
    0b011,
    0b111,
    0b000,
    0b100,
    0b010,
    0b110,
    0b000,
    0b000,
    0b000,
    0b000,
    0b000,
]

# 2D matrix for servo positions[servo#][up, down, or clear]
positions = [[55, 78, 0], 
             [45, 22, 100], 
             [45, 25, 100]
             ]

up_valve = 0
down_valve = 1
clear_valve = 2


while True:
    index = 0

    # Read digital inputs and compute index
    if not n_switch.value:
        index += 0b1000
    if not s_switch.value:
        index += 0b0100
    if not e_switch.value:
        index += 0b0010
    if not w_switch.value:
        index += 0b0001

    # Fetch valve state from lookup table
    valve_state = valve_lut[index]

    # Debug output
    print(
        "Inputs: N={} S={} W={} E={}".format(
            (not n_switch.value),
            (not s_switch.value),
            (not w_switch.value),
            (not e_switch.value),
        )
    )
    print(f"Index: {index}  Valve State: {valve_state:03b}")

    # Set servo angles
    kit.servo[0].angle = (
        positions[0][down_valve] if (valve_state & 4) else positions[0][up_valve]
    )
    kit.servo[1].angle = (
        positions[1][down_valve] if (valve_state & 2) else positions[1][up_valve]
    )
    kit.servo[2].angle = (
        positions[2][down_valve] if (valve_state & 1) else positions[2][up_valve]
    )

    # Print resulting servo angles
    print(f"Servo 0 angle: {kit.servo[0].angle}")
    print(f"Servo 1 angle: {kit.servo[1].angle}")
    print(f"Servo 2 angle: {kit.servo[2].angle}")
    print("-" * 30)

    time.sleep(0.1)
