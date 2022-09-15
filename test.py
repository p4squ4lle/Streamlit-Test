from serial.tools import list_ports
import serial
import time

ser = serial.Serial('COM8', 9600, timeout=1)
ports = list_ports.comports()
serPortsDescription = [p.description for p in ports]
ser1 = ports[1].description
port = ports[serPortsDescription.index(ser1)].device
print(ser1)
print(port)

time.sleep(1)
ser.close()
