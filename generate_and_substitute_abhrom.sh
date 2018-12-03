#mkprom2 -leon3 -freq 70 -ddrram 128 -ddrfreq 140 -baud 38377 prog.o -o prom.rom
#sparc-elf-as $1 -o prog.exe
#sparc-elf-gcc -msoft-float -g -nostdlib prog.o -o prog.exe
#sparc-elf-objdump -s bprom.exe  > dump.prom
#python3 dump_filter.py < dump.prom > dump.prom.filtered
sparc-elf-objdump -sj .text $1 | tail -n +5  > dump.prom.filtered
python3 ahbrom_gen.py < dump.prom.filtered > ahbrom.vhd.gen
cp ahbrom.vhd.gen ../grlib-gpl-2018.3-b4226/designs/leon3-digilent-nexys4ddr/ahbrom.vhd
