import RPi.GPIO as gpio
import time
from sys import argv
import os
import subprocess

script,first = argv
print (first, 'seconds')
x = 0
y = int(first)
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(4,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(18,gpio.OUT)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setup(25,gpio.OUT)
while x< y:
    x = x+15
    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.HIGH)
    time.sleep(1)
    gpio.output(17,gpio.LOW)
    gpio.output(22,gpio.HIGH)
    time. sleep(1)
    gpio.output(22,gpio.LOW)
    gpio.output(4,gpio.HIGH)
    time.sleep(1)
    gpio.output(4,gpio.LOW)
    gpio.output(18,gpio.HIGH)
    time.sleep(1)
    gpio.output(18,gpio.LOW)
    gpio.output(17,gpio.HIGH)
    time.sleep(1)
    gpio.output(25,gpio.LOW)
    gpio.output(23,gpio.HIGH)
    time.sleep(1)
    gpio.output(17,gpio.LOW)
    gpio.output(22,gpio.HIGH)
    time. sleep(1)
    gpio.output(22,gpio.LOW)
    gpio.output(4,gpio.HIGH)
    time.sleep(1)
    gpio.output(4,gpio.LOW)
    gpio.output(18,gpio.HIGH)
    time.sleep(1)
    gpio.output(18,gpio.LOW)
    gpio.output(17,gpio.HIGH)
    time.sleep(1)
    gpio.output(23,gpio.LOW)
    gpio.output(24,gpio.HIGH) 
    time.sleep(1)
    gpio.output(17,gpio.LOW)
    gpio.output(22,gpio.HIGH)
    time. sleep(1)
    gpio.output(22,gpio.LOW)
    gpio.output(4,gpio.HIGH)
    time.sleep(1)
    gpio.output(4,gpio.LOW)
    gpio.output(18,gpio.HIGH)
    time.sleep(1)
    gpio.output(18,gpio.LOW)
    gpio.output(17,gpio.HIGH)
    time.sleep(1)
    

else:
    os.system("gpio reset")
