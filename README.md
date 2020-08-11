# Time-Lapse RPi camera using stepper motor

raspberry pi camera talking through USB to arduino controlled stepper
using Raspberry Pi zero w and Adafruit Trinket M0

convert to movie with
ffmpeg -i img%04d.jpg -c:v libx264 -vf fps=30 -pix_fmt yuv420p out.mp4
