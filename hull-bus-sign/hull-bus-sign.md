# Hull Bus Terminal Signs: Making Pong on an old Dot-Matrix Display

1. [Introduction](#introduction)
2. [How to connect to a bunch of scary looking electronics](#how-to-connect-to-a-bunch-of-scary-looking-electronics)
   1. [Microchips](#microchips)
   2. [Soldering](#soldering)
   3. [Connected! But it doesn't work](#connected-but-it-doesnt-work)
3. [What is SPI?](#what-is-spi)
   1. [The fix!](#the-fix)
4. [An aside: Neonode touch](#an-aside-neonode-touch)
   1. [The natural conclusion: a theramin](#the-natural-conclusion-a-theramin)
   2. [Theramin + bus sign!](#theramin--bus-sign)
5. [The "Final Project" - Pong!](#the-final-project---pong)
6. [Conclusion](#conclusion)

## Introduction

![Picture of bus sign on a workbench. It is a long blu and black dot matrix display with the titles "Service", "Destination", and "Time"](images/hw_sign_closed.jpg)

![Picture of the bus sign with the front panel lifted. You can see the individual LED dot matrix panels.](images/hw_sign_open.png)

## How to connect to a bunch of scary looking electronics

![Closeup picture of the electronics behind one of the panels on the display. Four AS1100 chips are visible.](images/hw_sign_as1100-chips.jpg)

![Closeup of a ribbon cable connected to a PCB via a socket.](images/hw_sign_ribbon-cable.jpg)

### Microchips

![Screenshot from AS1100 datasheet showing chips joined to 8x8 dot matrix displays, and chained together, along with accompanying text.](images/sw_as1100_daisychain.png)

![Closeup picture of the pins of the ribbon cable, and the soldering pads on the bottom of the PCB. Both are correspondingly numbered.](images/hw_sign_ribbon-port_back.png)

![Closeup picture of the top of the PCB, showing the holes the ribbon cable enters.](images/hw_sign_ribbon-port_front.png)

### Soldering

![Picture of several loose stripped wires above an electronics workbench.](images/hw_wires_stripped.jpg)

![Closeup picture of wires soldered into the connection pads on the back of a PCB.](images/hw_sign_ribbon-board_back.jpg)

![Picture of the bus sign with several wires attached to it.](images/hw_setup_zoom.jpg)

![Closeup picture of an Arduino Elego Uno R3, with three wires connected into pins 8, 9, and 10.](images/hw_arduino_lonely.jpg)

### Connected! But it doesn't work

<video controls preload="none" poster="./images/videopre_sign_garbage.jpg" loop>
  <source src="./images/videoff_sign_garbage.mp4" type="video/mp4">
</video>

## What is SPI?

![Screenshot from AS1100 datasheet, showing SPI protocol as a timing diagram.](images/sw_as1100_serial-addressing-modes.png)

![Picture of workbench, showing all components to make bus sign work. Oscilloscope by the side connects to setup.](images/hw_setup_scoping.jpg)

![Closeup picture of oscilloscope probes attached to wires going into Arduino.](images/hw_arduino_probes.png)

![Digital image of oscilloscope trace. Above: yellow signal oscillating. Below: blue signal turning on and off less frequently.](images/sw_oscilloscope_bad-spi.png)

![Picture of oscilloscope screen, showing neat SPI trace.](images/hw_oscilloscope_trace.jpg)

![Picture of oscilloscope screen, showing SPI trace more zoomed out.](images/hw_oscilloscope_signal.jpg)

### The fix!

<video controls preload="none" poster="./images/videopre_sign_display-test.jpg" loop>
  <source src="./images/videoff_sign_display-test.mp4" type="video/mp4">
</video>

<video controls preload="none" poster="./images/videopre_sign_scrolling-text_fast.jpg" loop>
  <source src="./images/videoff_sign_scrolling-text_fast.mp4" type="video/mp4">
</video>

## An aside: Neonode touch

![Picture of Neonode touch components including usb cable, sensor bar, interface chip, and interface cable.](images/hw_neonode.jpg)

<video controls preload="none" poster="./images/videopre_neonode_proto.jpg" loop>
  <source src="./images/videoff_neonode_proto.mp4" type="video/mp4">
</video>

### The natural conclusion: a theramin

<video controls preload="none" poster="./images/videopre_neonode_theramin.jpg">
  <source src="./images/videoff_neonode_theramin.mp4" type="video/mp4">
</video>

### Theramin + bus sign!

![Picture of many wires plugged into a breadboard, Arduino, and interface board.](images/setup_wire_mess.jpg)

<video controls preload="none" poster="./images/videopre_both_jumpy-theramin.jpg">
  <source src="./images/videoff_both_jumpy-theramin.mp4" type="video/mp4">
</video>

## The "Final Project" - Pong!

<video controls preload="none" poster="./images/videopre_both_pong.jpg" loop>
  <source src="./images/videoff_both_pong.mp4" type="video/mp4">
</video>

![Picture of sign and electronics set up to play Pong on a workbench at Hull Makerspace.](images/output_pong.jpg)

## Conclusion
