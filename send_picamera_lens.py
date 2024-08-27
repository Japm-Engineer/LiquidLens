import cv2
import sys
import socket
import imutils
import imagezmq
from picamera2 import Picamera2
from Lens.liquid_lens_driver import LiquidLensDriver
import time

class InvalidVoltageException(Exception):
    "Raised when the input voltage is not between 0 and 255"
    pass

class InvalidInputsException(Exception):
    "Raised when the input number is less of two (voltage  address)"
    pass

try:
    if (len(sys.argv[1]) <= 2):
        raise InvalidInputsException
    
except InvalidInputsException:
    sys.exit("wrong number of inputs, test")

except InvalidVoltageException:
    sys.exit("Exception occurred: Invalid Voltage, it must be between 0 and 255")
    
try:
    if (int(sys.argv[1]) >= 0) and (int(sys.argv[1]) <=255):
        voltage = int(sys.argv[1])
    else:
        raise InvalidVoltageException

lens = LiquidLensDriver()
picam2 = Picamera2()
lens.d_write(voltage)
# (640 ,480)
# picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (1920, 1080)}, lores={"size" : (320, 240)}, display="lores"))
# picam2.configure(picam2.create_preview_configuration(raw={"size":(1640,1232)},main={"size": (640, 480)}))
fullres = (3280,2464)
outres = (820,616)
picam2.configure(picam2.create_video_configuration(raw={'size':fullres},main={'format': 'RGB888','size': outres}))
picam2.start()

# socket zmq
sender = imagezmq.ImageSender(connect_to='tcp://192.168.31.121:5555')
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