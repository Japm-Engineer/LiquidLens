import smbus

class LiquidLensDriver:
  def loadDriver(self):
      self.driver = smbus.SMBus(1)
      self.driver.write_byte(0b0100011, 0x00)
      print("Bus ready: ", self.driver)

  def __init__(self, initial=172):

      self.middlevoltage = initial

      self.loadDriver()

  def d_write(self, voltage=False, close=False):
      # global middlevoltage

      if close:
          self.driver.write_byte(0b0100011, 0x00)  # Shutdown code
          return

      if voltage:
          self.driver.write_byte(0b0100011, int(voltage) % 256)
      else:
          self.driver.write_byte(0b0100011, int(self.middlevoltage) % 256)

  def set_voltage(self, volt=False, shutdown=False):
      self.d_write(voltage=volt, close=shutdown)
      """
      if close:
          self.bus.write_byte(0b0100011, 0x00) # Shutdown code
      else:
          self.bus.write_byte(0b0100011, int(round(4.8846 * v - 47.846)) % 256)

       else:
           if close:
               ser.close()
           else:
               resp = ser.write(d_write(v))
               ans = ser.read(4) #Reading response from driver
       """