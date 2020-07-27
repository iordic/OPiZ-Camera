#! /bin/bash

# Servomotor test:
sleep 0.2

INIT=500000
END=2000000

val=$INIT

while [ $val -lt $END ]
do
    echo $val > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
    val=`expr $val + 5000`
    sleep 0.001
done

echo $INIT > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

