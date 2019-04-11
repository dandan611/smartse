#coding: utf-8

import wiringpi as pi
import time
import sys

BUZZER_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(BUZZER_PIN, pi.OUTPUT)

try:
  while True:
    pi.digitalWrite(BUZZER_PIN, pi.HIGH)
    time.sleep(0.5)
    pi.digitalWrite(BUZZER_PIN, pi.LOW)
    time.sleep(0.5)

except KeyboardInterrupt:
  pi.digitalWrite(BUZZER_PIN, pi.LOW)
  sys.exit(0)
