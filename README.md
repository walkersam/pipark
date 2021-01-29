# pipark

This is a project for using a Raspberry Pi 3, 2x ultrasonic distance sensors and a PIR motion sensor to be used as a fixed parking sensor.  The sensor readings are accessible using a webpage presented using Flask.  

The main programme is run from an Shell script (run.sh) which runs two python programmes simultaneously; the website (website.py) and the sensor script (sensor.py).   The sensor script writes to text files which are pulled every 0.1 second from the web page.  

While this isn't the most attractive solution to the problem, for the size and scale of the issue, it works well.  

My original plan was to have a webpage with an image of a car which dynamically moves depending on the distances from the garage wall, but I decided it'd be more useful to just show the distance reading in centimetres.  I also want to find a way of pulling data directly from the sensors and feeding it to the web page - but while using Flask (which acts in a wrapper within the script its run from) it didn't seem the most straight forward.  Alternatively I look to push data to a DB and can update it more frequently - again, for the size and scale of the project, writing out to a file seemed acceptable.

Below are links to the hardware used:

https://thepihut.com/products/ultrasonic-distance-sensor-hcsr04 

https://thepihut.com/products/pir-motion-sensor-module 

https://thepihut.com/products/raspberry-pi-breadboard-half-size 

https://thepihut.com/products/resistor-packs 

https://thepihut.com/products/thepihuts-jumper-bumper-pack-120pcs-dupont-wire 



Below are links to some tutorials I found useful:

https://projects.raspberrypi.org/en/projects/python-web-server-with-flask 

https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi 

https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio 

