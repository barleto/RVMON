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
rvmon -h
Usage:
    rvmon device baudrate [-u]
    - device: device file name, e.g. /dev/ttyUSB1
    - baudrate: The parameter baudrate can be one of the standard values: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800,         2400, 4800, 9600, 19200, 38400, 57600, 115200. These are well supported on all platforms.
    
    -u: If set, the UART will be set in debug mode and will be redirected to RVMON. 
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
