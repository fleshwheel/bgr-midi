#!/usr/bin/env python3

import rtmidi
import time
from bgr import BGR

input = rtmidi.MidiIn()
output = rtmidi.MidiOut()

output.open_virtual_port("bgr output")
input.open_virtual_port("bgr input")
midi_offset = 36

reservoir = BGR(64)


def handle_input(event, data = None):
    message, dtime = event
    # - 48
    if message[0] == 0x90:
        reservoir.nodes[message[1] - 48] = True
        reservoir.lock[message[1] - 48] = True
    elif message[0] == 0x80:
        reservoir.nodes[message[1] - 48] = False
    
    print(message, dtime, data)

input.set_callback(handle_input)

while True:
    for note in range(16):
        if reservoir.nodes[note]:
            output.send_message([0x90, midi_offset + note, 127])
        else:
            output.send_message([0x80, midi_offset + note, 0])
    reservoir.iter()
    print(reservoir.nodes)
    time.sleep(0.05)

    
