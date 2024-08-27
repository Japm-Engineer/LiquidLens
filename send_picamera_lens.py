import cv2
import socket
import imutils
import imagezmq
from picamera2 import Picamera2
from Lens.liquid_lens_driver import LiquidLensDriver
import time
import argparse

parser = argparse.ArgumentParser(description='Take video with liquid lens and zmq')
parser.add_argument('-v', '--voltage',nargs='?',const=172, type = int,default=172)      # option that takes a value
parser.add_argument('-i','--ip',nargs='?', const='192.168.31.121', type = str, default='192.168.31.121')
parser.add_argument('-x','--xsize',nargs='?', const=3280, type = int, default=3280)
parser.add_argument('-y','--ysize',nargs='?', const=3280, type = int, default=2464)
parser.add_argument('-r','--resize',nargs='?', const=0.25, type = float, default=0.25)
args = parser.parse_args()

# image parameters
fullres = (args.xsize,args.ysize)
outres = (int(args.resize*args.xsize),int(args.resize*args.ysize))
    
try:
    if (int(args.voltage) >= 0) and (int(args.voltage) <=255):
        voltage = int(args.voltage)
    else:
        raise InvalidVoltageException

except InvalidVoltageException:
    sys.exit("Exception occurred: Invalid Voltage, it must be between 0 and 255")

adr = str(args.ip)
lens = LiquidLensDriver()
picam2 = Picamera2()
lens.d_write(voltage)

picam2.configure(picam2.create_video_configuration(raw={'size':fullres},main={'format': 'RGB888','size': outres}))
picam2.start()

# socket zmq
sender = imagezmq.ImageSender(connect_to=f'tcp://{adr}:5555')
rpi_name = socket.gethostname()
print(rpi_name)
print(type(rpi_name))
time.sleep(2.0)  # allow camera sensor to warm up

while True:
    im = picam2.capture_array()
    sender.send_image(rpi_name, im)
    #cv2.imshow("preview", frame)
    #rval, frame = vc.read()
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break