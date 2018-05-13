from socket import socket
from picamera import PiCamera
from time import sleep
from gpiozero import Button,LED
import datetime

led = LED(18)
button = Button(17)
camera = PiCamera()

camera.exposure_mode= 'antishake'
button.wait_for_press()
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image4.jpg')
camera.stop_preview()
