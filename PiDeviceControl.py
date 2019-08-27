import RPi.GPIO as GPIO
import time
trigger_pin = 23
echo_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    distance_in = distance_cm / 2.5
    #return (distance_cm, distance_in)
    return distance_cm

def PiDevice_GetChoInBo_Distance():
    return get_distance()

#####################################################

trigger_pin_2 = 27
echo_pin_2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_2, GPIO.OUT)
GPIO.setup(echo_pin_2, GPIO.IN)

def send_trigger_pulse_2():
    GPIO.output(trigger_pin_2, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin_2, False)

def wait_for_echo_2(value, timeout):
    count = timeout
    while GPIO.input(echo_pin_2) != value and count > 0:
        count = count - 1

def get_distance_2():
    send_trigger_pulse_2()
    wait_for_echo_2(True, 5000)
    start = time.time()
    wait_for_echo_2(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    return distance_cm

def PiDevice_GetChoInBo_Distance_2():
    return get_distance_2()

###########################################

import picamera
import time

def PiDevice_GetCamera_Picture():
    camera = picamera.PiCamera()
    camera.resolution = (224, 224)
    time.sleep(5) # Camera warm-up time
    camera.capture('trash.png')


#####################################
import time
 
CONTROL_PIN = 17
PWM_FREQ = 50
STEP=15
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)

def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle

def PiDevice_Move4FuMata(angle):
    dc = angle_to_duty_cycle(angle)
    pwm.ChangeDutyCycle(dc)
