# Delete implict rules
.SUFFIXES:

# Determine the directory where this Makefile is located
MFD = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

cross=arm-eabi-
cpu=arm926ej-s

CC=$(cross)gcc
LD=$(cross)ld
OC=$(cross)objcopy

cflags=-mcpu=$(cpu) -I. -Wall -O2 -g

.PHONY: all
all: test.bin

test.o: $(MFD)/test.c
	$(CC) $(cflags) -c -DBmArm -o $@ $^

startup.o: $(MFD)/startup.S
	$(CC) $(cflags) -DRESET_ON_MAIN_COMPLETE -c -o $@ $^

test.bin: test.o startup.o $(MFD)/link.make.ld
	$(LD) -T $(MFD)/link.make.ld test.o startup.o -o test.elf
	$(OC) -O binary test.elf test.bin

.PHONY: run
run: test.bin
	# -no-reboot allows a reset to exit qemu
	qemu-system-arm -M versatilepb -m 128M -nographic -no-reboot -kernel test.bin
  
.PHONY: clean
clean:
	rm -rf *.o *.elf *.bin
