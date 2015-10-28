# Delete implict rules
.SUFFIXES:

# Determine the directory where this Makefile is located
MFD = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

cflags=-I. -Wall -O2 -g

.PHONY: all
all: Posix

.PHONY: BmArm
BmArm: cross=arm-eabi-
BmArm: CFlagMArch=armv5te
BmArm: CFlagMTune=arm926ej-s
BmArm: Platform=BmArm
BmArm: CC=$(cross)gcc
BmArm: LD=$(cross)ld
BmArm: OC=$(cross)objcopy

BmArm: test.bin

.PHONY: Posix
Posix: cross=
Posix: CFlagMArch=native
Posix: CFlagMTune=native
Posix: Platform=Posix
Posix: CC=$(cross)gcc
Posix: LD=$(cross)ld
Posix: OC=$(cross)objcopy

Posix: test

test: test.Posix.o
	$(CC) $(cflags) test.$(Platform).o -o test

test.BmArm.o: $(MFD)/test.c
	$(CC) $(cflags) -march=$(CFlagMArch) -mtune=$(CFlagMTune) -c -D$(Platform) -o test.$(Platform).o $^

test.Posix.o: $(MFD)/test.c
	$(CC) $(cflags) -march=$(CFlagMArch) -mtune=$(CFlagMTune) -c -D$(Platform) -o test.$(Platform).o $^

startup.o: $(MFD)/startup.S
	$(CC) $(cflags) -DRESET_ON_MAIN_COMPLETE -c -o $@ $^

test.bin: test.BmArm.o startup.o $(MFD)/link.make.ld
	$(LD) -T $(MFD)/link.make.ld test.$(Platform).o startup.o -o test.elf
	$(OC) -O binary test.elf test.bin

.PHONY: run-posix
run-posix: Posix
	./test

.PHONY: run-bmarm
run-bmarm: BmArm
	# -no-reboot allows a reset to exit qemu
	qemu-system-arm -M versatilepb -m 128M -nographic -no-reboot -kernel test.bin
  
.PHONY: clean
clean:
	rm -rf *.o *.elf *.bin test
