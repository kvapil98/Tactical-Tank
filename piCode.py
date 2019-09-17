
#import statements
import time
from picamera import PiCamera
import serial

#setup camera and serial communication
ser = serial.Serial('/dev/ttyACM0',9600);
camera = PiCamera()

#setup infinite loop to always listen for serial input
while 1:
    #if received information then take a photo
    if(ser.in_waiting > 0):
        line = ser.readline()
        print(line)
        image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time()*1000))
        camera.capture(image_path)
        print('Took photo')


