# Delete implict rules
.SUFFIXES:

cross=arm-eabi-
cpu=arm926ej-s

CC=$(cross)gcc
LD=$(cross)ld
OC=$(cross)objcopy

cflags=-mcpu=$(cpu) -I. -Wall -O2 -g

.PHONY: all
all: test.bin

test.o: test.c
	$(CC) $(cflags) -c -o test.o test.c

startup.o: startup.S
	$(CC) $(cflags) -c -o startup.o startup.S

test.bin: test.o startup.o
	$(LD) -T link.ld test.o startup.o -o test.elf
	$(OC) -O binary test.elf test.bin

.PHONY: run
run: test.bin
	qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin
  
.PHONY: clean
clean:
	rm -rf *.o *.elf *.bin
