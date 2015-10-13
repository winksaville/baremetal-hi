# Delete implict rules
.SUFFIXES:

cross=arm-eabi-
cpu=arm926ej-s

CC=$(cross)gcc
LD=$(cross)ld
AS=$(cross)as
OC=$(cross)objcopy

cflags=-mcpu=$(cpu) -I. -Wall
aflags=-mcpu=$(cpu) -I. -Wall

.PHONY: all
all: test

test.o: test.c
	$(CC) $(cflags) -c -o test.o test.c

startup.o: startup.s
	$(AS) $(aflags) -c -o startup.o startup.s

test: test.o startup.o
	$(LD) -T link.ld test.o startup.o -o test.elf
	$(OC) -O binary test.elf test.bin

.PHONY: run
run: test
	qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin
  
.PHONY: clean
clean:
	rm -rf *.o *.elf *.bin
