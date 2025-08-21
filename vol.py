
from Lens.liquid_lens_driver import LiquidLensDriver
import argparse

parser = argparse.ArgumentParser(description='Take Images with liquid lens')
parser.add_argument('-v', '--voltage',nargs='?',const=172, type = int,default=172)  
parser.add_argument('-x','--xsize',nargs='?', const=3280, type = int, default=3280)
parser.add_argument('-y','--ysize',nargs='?', const=2464, type = int, default=2464)
parser.add_argument('-r','--resize',nargs='?', const=1, type = float, default=1)
args = parser.parse_args()

try:
    if (int(args.voltage) >= 0) and (int(args.voltage) <=255):
        voltage = int(args.voltage)
    else:
        raise InvalidVoltageException
except InvalidVoltageException:
    sys.exit("Exception occurred: Invalid Voltage, it must be between 0 and 255")

lens = LiquidLensDriver()
lens.d_write(voltage)
