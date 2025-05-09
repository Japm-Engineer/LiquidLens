import subprocess
import os, argparse, time
from Lens.liquid_lens_driver import LiquidLensDriver
import numpy as np

parser = argparse.ArgumentParser(description='record image using libcamera-still')
parser.add_argument('-v', '--voltage',nargs='?',const=172, type = int,default=172)  
parser.add_argument('-g', '--gain',nargs='?',const=1, type = float,default=1)  
parser.add_argument('-exp','--exposure',nargs='?', const=100, type = float, default=100)
parser.add_argument('-n','--number',nargs='?', const=3, type = int, default=3)
parser.add_argument('-t','--text',nargs='?', const="", type = str, default="")
parser.add_argument('-d','--delay',nargs='?', const=0, type = float, default=0)
args = parser.parse_args()

lens = LiquidLensDriver()
try:
    if (int(args.voltage) >= 0) and (int(args.voltage) <=255):
        voltage = int(args.voltage)
    else:
        raise InvalidVoltageException
except InvalidVoltageException:
    sys.exit("Exception occurred: Invalid Voltage, it must be between 0 and 255")

ground = '/home/pi/Documents/'
pathground = "liquidimg/"
pathday = time.strftime("%Y%m%d") 
Time = time.strftime("%H%M%S")

if ('liquidimg' in os.listdir(ground)) == False:
    os.mkdir(ground + pathground)

pathground = ground + pathground
if (pathday in os.listdir(pathground)) == False:
    os.mkdir(time.strftime(pathground + pathday))
    
if args.text == "":
    path = pathground + pathday +'/'
voltage = np.arange(1,255,round(255/int(args.number)))

for v in voltage:
    file0 = path + Time + f"_cam0_g{args.gain}_exp{args.exposure}_voltage{v:d}.png"
    rpistr = f"libcamera-still -n -t 1 -e png -o {file0} --shutter {args.exposure*1000} --gain {args.gain} > /dev/null 2>&1"
    p = subprocess.Popen(rpistr, shell=True, stdout=subprocess.PIPE)
    p.wait()