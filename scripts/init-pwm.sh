#! /bin/bash

# Enable pwm0 (pwm1 doesn't work on armbian):
echo 0 > /sys/class/pwm/pwmchip0/export

# Configuration:
echo 20000000 > /sys/class/pwm/pwmchip0/pwm0/period
echo 500000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

echo "normal" > /sys/class/pwm/pwmchip0/pwm0/polarity
echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable

# Seek at begin:
sleep 0.2
val=500000

echo $val > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

# Add permisions for writing:
chmod 666 /sys/class/pwm/pwmchip0/pwm0/duty_cycle

