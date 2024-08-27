from picamera2 import Picamera2
import time,os, glob
from Lens.liquid_lens_driver import LiquidLensDriver
import argparse

parser = argparse.ArgumentParser(description='Take Images with liquid lens')
parser.add_argument('-v', '--voltage',nargs='?',const=172, type = int,default=172)  
parser.add_argument('-x','--xsize',nargs='?', const=3280, type = int, default=3280)
parser.add_argument('-y','--ysize',nargs='?', const=3280, type = int, default=2464)

args = parser.parse_args()

try:
    if (int(args.voltage) >= 0) and (int(args.voltage) <=255):
        voltage = int(args.voltage)
    else:
        raise InvalidVoltageException

except InvalidVoltageException:
    sys.exit("Exception occurred: Invalid Voltage, it must be between 0 and 255")

if (time.strftime("%Y%m%d") in os.listdir()) == False:
    os.mkdir(time.strftime("%Y%m%d"))


path = time.strftime("%Y%m%d")
files = glob.glob(path+f"/Liquidlens_voltage{voltage:d}*.jpg")
length = len(files)

lens = LiquidLensDriver()
lens.d_write(voltage)
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size":(args.xsize,args.ysize)})
picam2.configure(camera_config)

picam2.start()
time.sleep(2)
picam2.capture_file(f"{path}/Liquidlens_voltage{voltage:d}_{length+1:0>3.0f}.jpg")
print(f"Image name:Liquidlens_voltage{voltage:d}_{length+1:0>3.0f}.jpg")