import wiringpi as pi
import time
import sys

LED_PIN = 23
SW_PIN = 24
BUZZER_PIN = 18

STANDBY = 1
COUNTUP = 2
NOTICE = 3

if __name__ == '__main__':

    pi.wiringPiSetupGpio()
    pi.pinMode(LED_PIN, pi.OUTPUT)
    pi.pinMode(SW_PIN, pi.INPUT)
    pi.pullUpDnControl(SW_PIN, pi.PUD_UP)
    pi.pinMode(BUZZER_PIN, pi.OUTPUT)

    timec = 0
    state = 1

    try:
        while True:

            if (state == STANDBY):
                print("STANDBY")
                if (pi.digitalRead(SW_PIN) == pi.LOW):
                    state = 2

                time.sleep(0.1)

            elif (state == COUNTUP):
                print('{}秒経過\n'.format(timec))
                if (timec >= 18):
                    state = 3
                    timec = 0
                    pi.digitalWrite(LED_PIN, pi.HIGH)
                    pi.digitalWrite(BUZZER_PIN, pi.HIGH)
                else:
                    time.sleep(1.0)
                    timec += 1

            elif (state == NOTICE):
                print("180秒経過しました")
                if (pi.digitalRead(SW_PIN) == pi.LOW):
                    state = 1
                    pi.digitalWrite(BUZZER_PIN, pi.LOW)
                    pi.digitalWrite(LED_PIN, pi.LOW)
                    time.sleep(1.0)

                else:
                    if(pi.digitalRead(LED_PIN) == pi.LOW):
                        pi.digitalWrite(LED_PIN, pi.HIGH)
                    else:
                        pi.digitalWrite(LED_PIN, pi.LOW)

                time.sleep(0.1)

            else:
                pass

    except KeyboardInterrupt:
        pi.digitalWrite(LED_PIN, pi.LOW)
        pi.digitalWrite(BUZZER_PIN, pi.LOW)
        sys.exit(0)
