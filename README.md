# Adapted_Euphonium
​Robin Amend at https://amendmusiccenter.com​ made the first joystick-adapted euphonium in 1999, for a middle-school student in Mead, Washington. 

https://amendmusiccenter.com/assistive-technologies



​​​​In 2018, Robin received a request for an adapted euphonium, from a student in Illinois. He asked the students at the Spokane NEWTech Skill Center for help designing and building it.​
 ​

​​​​Our first prototype used an Adafruit 32u4 Feather board

https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le

with a PWM add-on board

https://www.adafruit.com/product/2928​ 

to interpret the joystick input and drive solenoids on the euphonium valves. This worked, but the frequency of the Pulse Width Modulation (PWM) signal caused the solenoids to make an audible buzz when held active at a reduced power level.



We changed to an Adafruit nRF52 Feather board 

https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide

which can do higher-frequency PWM without needing any add-on board.



Robin Amend wants to use an arcade joystick as the musician's user interface to control the system. It has 4 momentary mechanical switches. 

see the coding process in the Wiki
