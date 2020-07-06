from sys import argv
from os import mkdir
import serial
from time import sleep
from picamera import PiCamera


def step_enable(enable):
    with serial.Serial('/dev/ttyACM0',115200) as ser:
        ser.write(f"{'en'*enable or 'dis'}".encode('utf-8'))
    sleep(2)


def serial_send(to_send):
    with serial.Serial('/dev/ttyACM0',115200) as ser:
        ser.write(f"{to_send}\n".encode('utf-8'))


def create_dir():
    name = 'default'
    if len(argv) > 1:
        name = argv[1]
    else: raise Exception('add dir name')
    mkdir(name)
    return(name)


def main():
    dir_name = create_dir()
    camera = PiCamera()
    camera.resolution = (1024, 768)
    step_enable(True)
    sleep(2)

    for n, step in enumerate(range(0, 2400, 2), 1):
        sleep(1)
        camera.capture(f'{dir_name}/img{str(n).zfill(4)}.jpg')
        serial_send(step)

    sleep(2)
    step_enable(False)


if __name__ == "__main__":
    main()
