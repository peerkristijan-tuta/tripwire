import random
import time
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("localhost", port=5020)
client.connect()

while True:
    result = client.read_holding_registers(0, 2, slave=1)
    r1 = result.registers[0]
    r2 = result.registers[1]
    print("Registers:", r1, r2)
    if r1 % 2 == 0:
        print("Register 1 is even, setting coil to 0")
        client.write_coil(0, False, slave=1)
        break
    time.sleep(1)

client.close()