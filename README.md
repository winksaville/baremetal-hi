Bare Metal Hi

A bare metal test app that prints "Hi" to the Uart on the qemu Virtual
Development board for ARM.

Prior to building you need an arm-eabi cross compiler. One way is to follow
the instructions [here](https://github.com/winksaville/sortie-dopsys-myos) changing
'i586-elf' to 'arm-eabi'. TODO: Create a project to make it easier to create
cross-compilers and also add a gdb.

Then to build test.bin:
```
make
```
To run using QEMU:
```
make run
```
To exit from QEMU type (ctrl-a) then the letter 'x'
---
To use CMake, which is patterned after [this post](http://www.valvers.com/open-software/raspberry-pi/step03-bare-metal-programming-in-c-pt3/) do the following:
```
mkdir build-make
cd build-make
cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=../toolchain-arm-eabi.cmake ..
make
qemu-system-arm -M versatilepb -m 128M --nographic --kernel test.bin
```
Again, to exit from QEMU type (ctrl-a) then the letter 'x'
