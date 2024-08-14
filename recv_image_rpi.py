# recv image from rpi imagezmp socket
import cv2
import imagezmq
import subprocess
import zmq

context = zmq.Context()

image_hub = imagezmq.ImageHub()

#cv2.namedWindow("preview")
#print("antes")
while True:  # show streamed images until Ctrl-C
    #print("despues")
    rpi_name, image = image_hub.recv_image()
    #print("rpi")
    cv2.imshow(rpi_name, image)  # 1 window for each RPi
    image_hub.send_reply(b'OK')
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        image_hub.send_reply(b'ERROR')
        break