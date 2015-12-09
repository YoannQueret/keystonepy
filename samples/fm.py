import keystone.radio as radio
import keystone.constants as constants
import keystone.program as program

import sys

with radio.Radio("/dev/ttyACM0", mode=constants.FM) as r:
    # Set the volume to 6 (Max is 16)
    r.volume = 6

    # Request stereo sound
    r.stereo = True

    p = program.Program(r, constants.FM, int(sys.argv[1]))
    p.play()

    while True:
        r.status
        text = p.name
	if text!='':
        	print text
