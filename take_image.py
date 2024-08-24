from picamera2 import Picamera2
import sys
import time,os, glob
from Lens.liquid_lens_driver import LiquidLensDriver

class InvalidVoltageException(Exception):
    "Raised when the input voltage is not between 0 and 255"
    pass

try:
    if (int(sys.argv[1]) >= 0) and (int(sys.argv[1]) <=255):
        voltage = int(sys.argv[1])
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
#camera_config = picam2.create_preview_configuration()
camera_config = picam2.create_still_configuration(main={"size":(3280,2464)})
picam2.configure(camera_config)

picam2.start()
time.sleep(2)
picam2.capture_file(f"{path}/Liquidlens_voltage{voltage:d}_{length+1:0>3.0f}.jpg")
print(f"Image name:Liquidlens_voltage{voltage:d}_{length+1:0>3.0f}.jpg")