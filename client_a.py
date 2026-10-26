import random
import time
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("localhost", port=5020)
client.connect()

while True:
    coil = client.read_coils(0, 1, slave=1)
    if (coil.bits[0]):
        r1 = random.randint(1, 9)
        r2 = random.randint(1, 9)
        client.write_registers(0, [r1, r2], slave=1)
        print("Wrote registers:", r1, r2)
    else:
        print("Coil is 0, stopping")
        break
    time.sleep(2)

client.close()