# RVMON - ReonV Monitor

This is a monitor software to connect to the ReonV via UART.
The ReonV project can be found here: [ReonV](https://github.com/lcbcFoo/ReonV)

This project was made as a substitute for GRMON3, since it cannot work properly with Risc-V ISA.

__Note:__ This monitor was created based on the _Digilent Nexys4ddr_ FPGA board. So some features may not work properly in other boards.

As of now, RVMON only initializes DDR2 memory controller at start-up. Other controllers may be added in the future.

Feel free to use and extend RVMON as you wish.

## Requirements

You need Python3, with the following python3 libs installed:
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


### Commands

To get a list of available commands:
```
RVMON> help

Documented commands (type help <topic>):
========================================
conn  fix  help  i  load  q  replay  run  sr  srecl  sw

```

All commands has some kind of help, built-in to RVMON. Just type:
```
RVMON> help commandName
```
