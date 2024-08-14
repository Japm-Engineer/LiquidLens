import cv2
import socket
import imutils
import imagezmq
from picamera2 import Picamera2
from Lens.liquid_lens_driver import LiquidLensDriver
import time
impor

lens = LiquidLensDriver()
picam2 = Picamera2()
lens.d_write(0)
# (640 ,480)
# picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (1920, 1080)}, lores={"size" : (320, 240)}, display="lores"))
# picam2.configure(picam2.create_preview_configuration(raw={"size":(1640,1232)},main={"size": (640, 480)}))
fullres = (3280,2464)
outres = (820,616)
picam2.configure(picam2.create_video_configuration(raw={'size':fullres},main={'format': 'RGB888','size': outres}))
picam2.start()

# socket zmq
sender = imagezmq.ImageSender(connect_to='tcp://192.168.31.120:5555')
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