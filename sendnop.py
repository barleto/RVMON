import serial
import sys

ser = ser = serial.Serial(sys.argv[1])
ser.write(b"\x00")
