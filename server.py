from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSequentialDataBlock

class CallbackBlock(ModbusSequentialDataBlock):
    def setValues(self, address, values):
        if address == 0 and values[0] == 0:
            print("Coil set to 0 - writing 9.9 to registers")
            registers.setValues(0, [9, 9])
        super(CallbackBlock, self).setValues(address, values)

coils = CallbackBlock(0, [1])
registers = ModbusSequentialDataBlock(0, [0, 0])

store = ModbusSlaveContext(co=coils, hr=registers, zero_mode=True)
context = ModbusServerContext(slaves=store, single=True)

print("Server running on port 5020")
StartTcpServer(context=context, address=("localhost", 5020))