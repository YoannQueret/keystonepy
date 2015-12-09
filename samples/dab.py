#! /usr/bin/python
from keystone.radio import Radio
import time

program_index = 0

with Radio("/dev/ttyACM0") as r:
    # Reset database
    r.reset
    
    # Search from 5A to 13F (See annexe A)
    print "Searching ..."
    r.dab_auto_search(clear=False)
    
    # Display service list
    print "-- SERVICES LIST --"
    i=0
    for p in r.programs:
        print "%s = name: %s (eid: %s, sid: %s), type: %s, application_type: %s" % (i, p.name, hex(p.info.ensemble_id), hex(p.info.service_id), p.type, p.application_type)
        i+=1
    
    print "----------"
    
    # Select the fourth program from the ensemble
    if program_index <= len(r.programs):
        program = r.programs[program_index]
    else:
        print "ERROR: Program %s can not be selected" % program_index
        exit()

    # Set the volume to 10 (Max is 16)
    r.volume = 6

    # Request stereo sound
    r.stereo = True

    # Play the selected program
    program.play()

    # Print the name of the program
    print "-- NOW PLAYING : %s --" % program.name
    print "volume             : %s" % r.volume
    
    print "Ensemble ID        : %s" % hex(program.info.ensemble_id)
    print "Ensemble name      : %s" % r.ensemble_name(program_index, 'DAB')
    print "Service ID         : %s" % hex(program.info.service_id)
    
    while r.status != 0:
        #print 'wait ...'
        time.sleep(0.5)
    
    time.sleep(0.5)

    print "signal_strength    : %s" % r.signal_strength.strength
    print "dab_signal_quality : %s" % r.dab_signal_quality
    print "data_rate          : %skbps" % r.data_rate
        
    print "----------"
    
    
    
    # Wait for text from the program
    while True:
      if r.status != -1:
        text = program.text
        
        if text != None:
          print text