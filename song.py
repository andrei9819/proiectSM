import pigpio
import time
import RPi.GPIO as GPIO
import array

pi = pigpio.pi()

#notes frequency
c8 = 4187
b7 = 3951
a7 = 3520
g7 = 3136
f7 = 2794
e7 = 2637
d7 = 2349
c7 = 2093
b6 = 1975
a6 = 1760
g6 = 1568
f6 = 1397
e6 = 1318
d6 = 1174
c6 = 1046
b5 = 988
a5 = 880
g5 = 784
f5 = 698
e5 = 659
d5 = 587
c5 = 523
b4 = 494
a4 = 440
g4 = 392
f4 = 349
e4 = 330
d4 = 293
c4 = 261
b3 = 247
a3 = 220
g3 = 196
f3 = 174
e3 = 165
d3 = 146
c3 = 130
b2 = 123
a2 = 110
g2 = 97
f2 = 87
e2 = 82
d2 = 73
c2 = 65
b1 = 61
a1 = 55
g1 = 49
f1 = 43
e1 = 41
d1 = 37
c1 = 33

#pin used by the buzzer, GPIO18=pin 12
buzzer = 18
pi.set_mode(buzzer, pigpio.OUTPUT)
GPIO.setmode(GPIO.BOARD)

#pin numbers for the buttons
button1 = 18
button2 = 24
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#creating the first song
def song1():
    delay1 =0.6
    delay2 = 0.4
    delay3 = 0.3
    delay4 = 0.1
    #we are going to create 2 arrays
    #first array is for note sequence
    #second array is for  note length
    sequence_1_notes = array.array('i', [g7, e7, g7, g7, e7, g7])
    sequence_1_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1])

    for i in range(0,6):
        pi.hardware_PWM(buzzer, sequence_1_notes[i], 500000)
        time.sleep(sequence_1_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)


    sequence_2_notes = array.array('i', [a7, g7, f7, e7, d7, e7, f7])
    sequence_2_delays = array.array('f', [delay1, delay1, delay1, delay1, delay3, delay3, delay3])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_2_notes[i], 500000)
        time.sleep(sequence_2_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    sequence_3_notes = array.array('i', [a7, b7, d7, e7, e7, d7])
    sequence_3_delays = array.array('f', [delay1, delay1, delay2, delay1, delay1, delay2])

    for i in range(0,6):
        pi.hardware_PWM(buzzer, sequence_3_notes[i], 500000)
        time.sleep(sequence_3_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    sequence_4_notes = array.array('i', [d7, g7, g7, a7, e7, e7, g7])
    sequence_4_delays = array.array('f', [delay3, delay3, delay3, delay2, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_4_notes[i], 500000)
        time.sleep(sequence_4_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)


    sequence_5_notes = array.array('i', [a7, b7, b7, a7, a7, a7, b7])
    sequence_5_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_5_notes[i], 500000)
        time.sleep(sequence_5_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)


    sequence_6_notes = array.array('i', [c7, d7, d7, e7, d7, c7, e7])
    sequence_6_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_6_notes[i], 500000)
        time.sleep(sequence_6_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

#creating the second song
def song2():
    time0 = 0.1
    time1 = 0.3
    time2 = 0.6
    time3 = 0.5
    time4 = 0.4
    time5 = 0.2


    sequence_1_notes = array.array('i', [d4, a4, d4, c3, a4, e4, g4])
    sequence_1_delays = array.array('f', [time1, time1, time1, time1, time1, time1, time2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_1_notes[i], 500000)
        time.sleep(sequence_1_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


    sequence_2_notes = array.array('i', [c4, d4, e4, d4, e4])
    sequence_2_delays = array.array('f', [time1, time1, time1, time1, time3])

    for i in range(0,5):
        pi.hardware_PWM(buzzer, sequence_2_notes[i], 500000)
        time.sleep(sequence_2_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


    sequence_3_notes = array.array('i', [g3, c5, g2, d1, d4, a4, a4, g3])
    sequence_3_delays = array.array('f', [time4, time1, time1, time1, time4, time1, time1, time2])

    for i in range(0,8):
        pi.hardware_PWM(buzzer, sequence_3_notes[i], 500000)
        time.sleep(sequence_3_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


    sequence_4_notes = array.array('i', [a5, e5, a5, d5, c5])
    sequence_4_delays = array.array('f', [time1, time1, time1, time1, time3])

    for i in range(0,5):
        pi.hardware_PWM(buzzer, sequence_4_notes[i], 500000)
        time.sleep(sequence_4_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


    sequence_5_notes = array.array('i', [a3, b3,c4, c4, d4, g3, g4, c6, a3, c6])
    sequence_5_delays = array.array('f', [time5, time5, time1, time1, time1, time5, time5, time1, time1, time2])

    for i in range(0,10):
        pi.hardware_PWM(buzzer, sequence_5_notes[i], 500000)
        time.sleep(sequence_5_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


    sequence_6_notes = array.array('i', [a5, b5, c5, a5, c5, a4, a5])
    sequence_6_delays = array.array('f', [time1, time1, time1, time1, time1, time1, time2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_6_notes[i], 500000)
        time.sleep(sequence_6_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


try:
    while True:
        if GPIO.input(button1) == GPIO.LOW:
            song1()

        if GPIO.input(button2) == GPIO.LOW:
            song2()

except KeyboardInterrupt:
    pass


pi.write(buzzer, 0)
pi.stop()
GPIO.cleanup()
