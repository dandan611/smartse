#coding: utf-8

import wiringpi as pi
import time
import sys

LED_PIN = 23
SW_PIN = 24
BUZZER_PIN = 18


pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_UP)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)


try:
  while True:
    if (pi.digitalRead(SW_PIN) == pi.LOW):
      pi.digitalWrite(LED_PIN, pi.HIGH)
      pi.digitalWrite(BUZZER_PIN, pi.HIGH)
    else:
      pi.digitalWrite(LED_PIN, pi.LOW)
      pi.digitalWrite(BUZZER_PIN, pi.LOW)
    time.sleep(0.1)

except KeyboardInterrupt:
  pi.digitalWrite(BUZZER_PIN, pi.LOW)
  sys.exit(0)

