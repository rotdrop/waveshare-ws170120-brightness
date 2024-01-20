#!/usr/bin/env python

from hidraw import HIDRaw
from os import listdir
from glob import glob
# from hexdump import hexdump

class WaveshareWS170120:
  """
  Control the brightness of an Waveshare WS170120 touch-screen.
  """
  _ws170120Event = 'usb-WaveShare_WS170120_220211-event-if00'
  _ws170120Vendor = 0x0eef
  _ws170120Product = 0x0005

  _dataLength = 38
  _brightnessAddress = 6
  _controlMagic = bytearray([0x04, 0xaa, 0x01, 0x00])

  def __init__(self, verbosity):
    """
    Initialize this instance with the first found Waveshare WS170120 touch-screen.
    verbosity (int)
        Control the verbosity of the actions. Currently unused.
    """
    self._verbosity = verbosity
    self._findDevice()
    self._dataBuffer = self._controlMagic + bytearray(self._dataLength - len(self._controlMagic))

  def setBrightness(self, percentage):
    """
    percentage
        Set the brightness of the Waveshare WS170120 touch-screen to the given percentage. Obviously,
        percentage should be non-negative and less or equal 100.
    """
    device = open(self._deviceName, 'rb+')
    self._dataBuffer[self._brightnessAddress] = percentage
    result = device.write(self._dataBuffer)
    if result != len(self._dataBuffer):
      raise IOError('Unexpected resulte %d from writing brightness data,expected %d.' % (result, len(self._dataBuffer)))
    if self._verbosity > 0:
      print('Brightness has been set to %d%%.' % percentage)
    
  def _findDevice(self):
    deviceGlob = '/sys/bus/hid/devices/*:' + f'{self._ws170120Vendor:0{4}x}'.upper() + ':' + f'{self._ws170120Product:0{4}x}'.upper() + '.*'
    sysNodes = glob(deviceGlob, recursive=False)

    if len(sysNodes) < 1:
      raise FileNotFoundError('Waveshare monitor WS170120 is not connected.')

    sysNode = sysNodes[0]
    hidrawList = listdir(sysNode + '/hidraw')

    if len(hidrawList) < 1:
      raise FileNotFoundError('Waveshare monitor WS170120 is not connected.')

    deviceName = '/dev/' + hidrawList[0]  
    device = open(deviceName, 'rb+')
    # os.set_blocking(device.fileno(), False)
    hidRawDevice = HIDRaw(device)
    displayName = hidRawDevice.getName()
    info = hidRawDevice.getInfo()
    physAddr = hidRawDevice.getPhysicalAddress()
    
    if info.vendor != self._ws170120Vendor or info.product != self._ws170120Product:
      raise FileNotFoundError('Waveshare monitor WS170120 is not connected.')

    # just remember the name
    device.close()
    
    self._deviceName = deviceName
    
if __name__ == '__main__':
  import argparse
    
  parser = argparse.ArgumentParser(
    description='Set the brightness of an attached Waveshare WS170120 touch-screen'
  )
  parser.add_argument(
    '-b', '--brightness',
    metavar='PERCENTAGE',
    type=int,
    required=True,
    help='set the brightness value to the given percentage.',
  )
  parser.add_argument(
    '-v', '--verbose',
    default=0,
    action='count',
  )

  args = parser.parse_args()

  brightness = args.brightness
  verbosity = args.verbose
  if verbosity > 0:
    print('Attempting to set brightness to %d%%.' % brightness)

  backlightController = WaveshareWS170120(verbosity)
  backlightController.setBrightness(brightness)
  



