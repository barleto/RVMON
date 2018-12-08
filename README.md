# RVMON - ReonV Monitor

This is a monitor software to connect to the ReonV via UART.
The ReonV project can be found here: [ReonV](https://github.com/lcbcFoo/ReonV)

This project was made as a substitute for GRMON3, since it cannot work properly with Risc-V ISA.

## Requirements

You need Python3, with the following oython3 libs installed:
- pyserial
- pyelftools
- bincopy
These libraries are easely installed with [__pip3__](https://pip.pypa.io/en/stable/installing/) or any other way to install python3 modules.

## Usage:
```
rvmon device baudrate [-u]
```
#### Example:
```bash
rvmon /dev/ttyUSB1 115200
```

### Basic serialCommandsFileName
#### load
