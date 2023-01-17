# System-Monitor
I used picobricks development board in this project.
picobricks is a development board developed by robotistan.com
For this project, raspberry pi pico and ssd1306 oled screen are also used.
I transferred the computer's cpu and ram values to picobricks.
I used python and micropython languages for this project.
I get the ram and cpu values of the computer in python with the psutil module.
Then i send these values from serial port to pico.
Raspberry Pi Pico prints incoming values to oled screen.
main.py runs on computer side serial.py runs on pico side.
