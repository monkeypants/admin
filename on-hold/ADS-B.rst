ADS-B receiver for sense-and-avoid of other aircraft 
====================================================

:ref:`TRL`: 3

Description: Using an ADS-B receiver to sense and avoid other aircraft in the area 

Developers: Tridge

Status - Hardware receiver works fine. Need to develop software to interpret messages and develop collision avoiding waypoints to send to the APM

The proof of concept receiver was made from a cheap USB digital TV receiver hardware, with this software:

https://github.com/bistromath/gr-air-modes

Running on GnuRadio:

http://gnuradio.org/


