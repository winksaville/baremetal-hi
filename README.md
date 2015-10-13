Bare Metal Hi

A bare metal test app that prints "Hi" to the Uart on the qemu Virtual
Development board for ARM.

Prior to building you need an arm-eabi cross compiler. One way is to follow
the instructions (here)[https://github.com/winksaville/sortie-dopsys-myos] changing
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
