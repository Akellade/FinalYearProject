FinalYearProject
================

Arduino & Python files

This is the software portion of my Engineering degree final year project.

Purpose:
  The arduino controls via 100kHz PWM a mosfet as part of a buck-boost DC-DC converter.
  Using Serial Comms, the arduino receives a power value, it compares it with a value calculated 
  from the circuit, and adjusts the PWM to increase/decrease the power output. 
  
  the Python program serves 3 roles; 
  
    1. Send required power from raw input, over serial to the arduino.
    
    2. Receive voltage / power readings from the arduino
    
    3. Saves the received data for later review. 
    
This is my first attempt using python/Github.
