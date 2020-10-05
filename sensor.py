import RPi.GPIO as GPIO
import time
GPIO.cleanup()

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)

    i=GPIO.input(26)

    f = open("/home/pi/website/templates/motiondetection.txt", "w")
    f.write(str(i))
    f.close()
    if i == 1:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        # Left sensor connected to pins 16 (TRIG) & 18 (ECHO)
        TRIG = 23
        ECHO = 24

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 1)
        print ("Left distance:", distance, "cm")
        pct1 = distance
        f = open("/home/pi/website/templates/left.txt", "w")
        f.write(str(pct1))
        f.close()
        GPIO.cleanup()
        time.sleep(0.1)

        GPIO.setmode(GPIO.BCM)
        # Right sensor connected to pins 22 (TRIG) & 24 (ECHO)
        TRIG = 25
        ECHO = 8

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 1)
        print ("Right distance:", distance, "cm")
        pct2 = distance
        f = open("/home/pi/website/templates/right.txt", "w")
        f.write(str(pct2))
        f.close()
        GPIO.cleanup()
        time.sleep(0.1)
    else:
        print("No motion")
        time.sleep(5)
