# Bare Metal Hi

A trivial bare metal test app that prints "Hi" to the Uart on the qemu Virtual
Development board for ARM. The resulting runnable output is "test.bin" and can
be tested by running with qemu-system-arm:
```
qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin
```
I'm also exploring various build systems as I'm trying to decide which to use
as my preferred build system in the future. At the moment I feel using a
meta-build system which generates [Ninja](https://martine.github.io/ninja/) code
is the best approach, but we'll see how it goes.

Currently the set of build systems I'm interested in are:
* [GNU Make](https://www.gnu.org/software/make/) (done)
* [CMake](https://cmake.org) (partially done)
* [Meson](https://mesonbuild.com) (Not workng)
* [Craftr](https://github.com/craftr-build/craftr) (TODO)

There are some prerequisites:
* An arm-eabi cross compiler. (For now see [here](https://github.com/winksaville/sortie-dopsys-myos)
and change 'i586-elf' to 'arm-eabi'). TODO: Create a project to make it easier to create
cross-compilers and also add a gdb.
* Install [Ninja](https://martine.github.io/ninja/)
* Install which ever build system you're interested.

Also, don't hesitate to provide pull requests or fork this project to
do your own exploration.
___
## To build using gnu make
Currently his has a hard coded path [issue #1]](https://github.com/winksaville/baremetal-hi/issues/1) so they'll need to be adjusted manually.
```
make
```
To run using QEMU:
```
make run
```
To exit from QEMU type (ctrl-a) then the letter 'x'
___
## To build using [CMake](https://cmake.org/), which is patterned after [this](http://www.valvers.com/open-software/raspberry-pi/step03-bare-metal-programming-in-c-pt3/):
```
mkdir build-make
cd build-make
cmake -G "Ninja" -DCMAKE_TOOLCHAIN_FILE=../toolchain-arm-eabi.cmake ..
ninja
qemu-system-arm -M versatilepb -m 128M --nographic --kernel test.bin
```
Again, to exit from QEMU type (ctrl-a) then the letter 'x'
___
## To use meson:
**NOT WORKING** [issue #2](https://github.com/winksaville/baremetal-hi/issues/2)
```
mkdir build-meson
cd build-meson
meson --cross-file ../arm-eabi-cross_file.txt ..
```
___
## To use Craftr:
**TODO** [issue #3](https://github.com/winksaville/baremetal-hi/issues/3)
___
